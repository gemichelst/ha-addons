# hadolint ignore=DL3007
FROM ghcr.io/home-assistant/base:latest

LABEL \
  io.hass.version="1.0.0" \
  io.hass.type="app" \
  io.hass.arch="aarch64|amd64|armhf|armv7|i386"

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# hadolint ignore=DL3018
RUN apk add --no-cache python3 py3-pip && \
    python3 -m venv $VIRTUAL_ENV && \
    pip install --no-cache-dir flask==3.1.1

COPY app/ /app/
COPY run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
