FROM nginx:1.29-alpine

RUN apk add --no-cache wget ca-certificates

COPY download-csd.sh /docker-entrypoint.d/download-csd.sh
RUN chmod +x /docker-entrypoint.d/download-csd.sh

ENV SITE_URL="https://csd.uoc.gr"

