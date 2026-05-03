#!/usr/bin/with-contenv bashio
set -euo pipefail

bashio::log.info "Starting Multi Repo Manager"

python3 -m http.server 8080 --directory /config/ha-addons-ui
