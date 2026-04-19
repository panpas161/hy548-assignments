FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY controller.py .

RUN useradd --uid 1000 --create-home --no-log-init kopf
USER 1000:1000

# Watch Greeting objects in every namespace (RBAC must allow cluster-wide access).
ENTRYPOINT ["python", "-m", "kopf", "run", "/app/controller.py", "--all-namespaces", "--verbose"]
