#!/usr/bin/with-contenv bashio
set -euo pipefail

bashio::log.info "Starting Multi Repo Manager..."

mkdir -p /config/multi-repo-manager

REPOS_FILE="/config/multi-repo-manager/repos.json"
if [ ! -f "${REPOS_FILE}" ]; then
  bashio::log.info "Creating empty repos.json..."
  echo '{"repositories":[]}' > "${REPOS_FILE}"
fi

exec python3 /app/main.py
