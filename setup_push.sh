#!/bin/zsh
# 1. Push-Script ausführbar machen
chmod +x "/Users/marvinkuppens/Documents/Claude/Projects/uncle marv/push.sh"

# 2. Kaputte push()-Einträge aus .zshrc entfernen
python3 - << 'PYEOF'
import re
path = '/Users/marvinkuppens/.zshrc'
with open(path, 'r') as f:
    c = f.read()
c = re.sub(r'\npush\s*\(\)\s*\{[\s\S]*?\n\}', '', c)
c = re.sub(r'\nalias push=.*', '', c)
with open(path, 'w') as f:
    f.write(c)
print("Alte push-Eintraege entfernt.")
PYEOF

# 3. Sauberen Alias hinzufügen
echo '\nalias push="/Users/marvinkuppens/Documents/Claude/Projects/uncle marv/push.sh"' >> ~/.zshrc

echo "✅ Setup fertig! Starte ein neues Terminal-Fenster und tippe: push"
