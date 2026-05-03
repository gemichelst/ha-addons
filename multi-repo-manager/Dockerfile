FROM ghcr.io/home-assistant/base:latest
# hadolint ignore=DL3007

LABEL \
  io.hass.version="1.0.0" \
  io.hass.type="app" \
  io.hass.arch="aarch64|amd64|armhf|armv7|i386"

# hadolint ignore=DL3018
RUN apk add --no-cache python3 py3-pip && \
    pip3 install --no-cache-dir flask==3.1.1

COPY app/ /app/
COPY run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
