FROM ghcr.io/qregistry/standard/python:3.10-alpine

WORKDIR /api

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/sh", "/api/runner.sh"]
