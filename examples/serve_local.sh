#!/usr/bin/env bash
# Clone G0DM0D3 (if needed) and serve it locally, the way the project docs
# describe: the whole app is index.html, so a static file server is all it needs.
set -euo pipefail

PORT="${GODMODE_PORT:-8000}"
DIR="${GODMODE_DIR:-G0DM0D3}"

if [ ! -d "$DIR" ]; then
  git clone https://github.com/elder-plinius/G0DM0D3 "$DIR"
fi

if [ ! -f "$DIR/index.html" ]; then
  echo "index.html not found in $DIR - is this the right checkout?" >&2
  exit 1
fi

echo "Serving $DIR on http://localhost:$PORT"
echo "Open it in a browser, then paste your OpenRouter API key in Settings."
echo "The key is stored in the browser's localStorage, not sent to this server."
cd "$DIR"
exec python3 -m http.server "$PORT"
