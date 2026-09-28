#!/usr/bin/env sh
# Combine the new pages with the generated speaker pages and serve them locally.
# Usage: sh preview.sh   then open http://localhost:8000/
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="$HERE/../preview-site"
rm -rf "$OUT" && mkdir -p "$OUT"
cp -R "$HERE/index.html" "$HERE/assets" "$HERE/agenda" "$HERE/delegate" "$HERE/partners" "$OUT/"
( cd "$HERE/../speakers" && python3 build_speakers.py --out "$OUT/_spk" --base-url http://localhost:8000 >/dev/null )
cp -R "$OUT/_spk/speakers" "$OUT/speakers" && rm -rf "$OUT/_spk"
echo "Serving $OUT at http://localhost:8000/"
python3 -m http.server 8000 --directory "$OUT"
