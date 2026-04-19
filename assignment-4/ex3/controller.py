#!/usr/bin/env python

import base64
import copy
import os
import ssl

import jsonpatch
from flask import Flask, jsonify, request

app = Flask(__name__)


def inject_label(yaml_data, label):
    for part in yaml_data:
        if "labels" not in part["metadata"]:
            part["metadata"]["labels"] = {}
        part["metadata"]["labels"][label] = "true"


@app.route("/mutate", methods=["POST"])
def mutate():
    data = request.get_json()
    uid = data["request"]["uid"]
    service = copy.deepcopy(data["request"]["object"])
    inject_label([service], os.getenv("CUSTOM_LABEL", "custom-label"))
    patch = jsonpatch.JsonPatch.from_diff(data["request"]["object"], service)
    encoded_patch = base64.b64encode(patch.to_string().encode("utf-8")).decode("utf-8")

    return jsonify(
        {
            "apiVersion": "admission.k8s.io/v1",
            "kind": "AdmissionReview",
            "response": {
                "uid": uid,
                "allowed": True,
                "status": {"message": "Adding extra label"},
                "patchType": "JSONPatch",
                "patch": encoded_patch,
            },
        }
    )


def _ssl_context():
    cert = os.environ.get("TLS_CERT_FILE", "/etc/ssl/keys/tls.crt")
    key = os.environ.get("TLS_KEY_FILE", "/etc/ssl/keys/tls.key")
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    ctx.load_cert_chain(certfile=cert, keyfile=key)
    return ctx


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "443"))
    app.run(host="0.0.0.0", port=port, ssl_context=_ssl_context())
