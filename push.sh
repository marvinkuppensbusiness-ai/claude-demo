#!/bin/zsh
cd "/Users/marvinkuppens/Documents/Claude/Projects/uncle marv"
git add -A
git commit -m "Update $(date '+%d.%m.%Y %H:%M')" || true
git push origin gh-pages
echo "✅ Live auf travelwithmarv.de"
