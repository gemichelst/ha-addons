FROM ghcr.io/home-assistant/base:latest

LABEL \
  io.hass.version="1.0.0" \
  io.hass.type="app" \
  io.hass.arch="aarch64|amd64|armhf|armv7|i386"

RUN apk add --no-cache python3 py3-pip && \
    pip3 install --no-cache-dir flask

COPY app/ /app/
COPY run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
