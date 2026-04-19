FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY controller.py .

ENV PORT=443 \
    TLS_CERT_FILE=/etc/ssl/keys/tls.crt \
    TLS_KEY_FILE=/etc/ssl/keys/tls.key

EXPOSE 443

CMD ["python", "/app/controller.py"]
