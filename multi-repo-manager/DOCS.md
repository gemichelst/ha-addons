# Multi Repo Manager – Documentation

## What it does
- Add repository URLs with a name and optional description
- Enable / Disable entries
- Remove entries you no longer need
- Copy repository URLs to clipboard
- Open in Home Assistant via my.home-assistant.io deeplink

## Storage
All data is stored in `/addon_configs/<REPO>_multi_repo_manager/repos.json`.

## REST API

### GET /api/repos
Returns the current repository list as JSON.

### POST /api/repos
Body: `{ "name": "...", "url": "https://github.com/...", "description": "...", "enabled": true }`

## Support
https://github.com/gemichelst/ha-addons/issues
