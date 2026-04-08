#!/bin/zsh
cd "/Users/marvinkuppens/Documents/Claude/Projects/uncle marv"
git add -A
git commit -m "Update $(date '+%d.%m.%Y %H:%M')" 2>&1 | grep -v "nothing to commit" || echo "Keine neuen Aenderungen."
git push origin main
git push origin main:gh-pages
echo "✅ Live auf travelwithmarv.de"
