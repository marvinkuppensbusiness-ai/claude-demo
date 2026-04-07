#!/usr/bin/env python3
"""
UncleMarv — LemonSqueezy Product Setup Script
=============================================
Erstellt alle 9 Produkte + 1 Bundle automatisch im LemonSqueezy-Store
und gibt die fertigen Checkout-URLs aus.

Voraussetzungen:
  pip install requests

Benutzung:
  python3 setup_lemonsqueezy.py YOUR_API_KEY

API-Key holen: https://app.lemonsqueezy.com/settings/api
"""

import sys, json, time, re
try:
    import requests
except ImportError:
    print("Fehlende Bibliothek. Bitte ausführen: pip install requests")
    sys.exit(1)

# ─── Produktdefinitionen ────────────────────────────────────────────────────
PRODUCTS = [
    {
        "key":         "wallpaper",
        "name":        "UncleMarv World 4K",
        "description": "Stunning 4K travel wallpapers shot around the world. "
                       "40+ hand-picked photos in ultra-high resolution — mountains, "
                       "coastlines, cities and hidden gems. Perfect for desktop & mobile.",
        "price_cents": 999,   # €9.99
    },
    {
        "key":         "luts",
        "name":        "UncleMarv Film Grade",
        "description": "Cinematic LUT pack for video creators. 20 professionally crafted "
                       "colour grades inspired by film photography and golden-hour travel "
                       "footage. Compatible with Premiere, DaVinci Resolve & more.",
        "price_cents": 1999,  # €19.99
    },
    {
        "key":         "presets",
        "name":        "UncleMarv Filter Reset",
        "description": "Lightroom & Lightroom Mobile preset collection. 30 travel presets "
                       "covering every mood — warm sunsets, crisp mornings, moody streets. "
                       "One-click look, fully adjustable.",
        "price_cents": 1999,  # €19.99
    },
    {
        "key":         "guide",
        "name":        "UncleMarv Hack Pack",
        "description": "The ultimate travel hacks PDF guide. 50+ field-tested tips on "
                       "flights, accommodation, packing, money, safety and connectivity. "
                       "Saves you time, money and stress on every trip.",
        "price_cents": 799,   # €7.99
    },
    {
        "key":         "packing",
        "name":        "UncleMarv Pack List",
        "description": "The definitive packing checklist. Interactive PDF covering gear, "
                       "clothing, tech, toiletries and documents for every trip type — "
                       "carry-on only to 3-week adventure.",
        "price_cents": 499,   # €4.99
    },
    {
        "key":         "airport",
        "name":        "UncleMarv Gate Pass",
        "description": "Airport hacks & lounge guide. Everything you need to know about "
                       "priority boarding, lounge access, fast-track security and hidden "
                       "airport gems. Never stress at an airport again.",
        "price_cents": 299,   # €2.99
    },
    {
        "key":         "budget",
        "name":        "UncleMarv Capsule Kit",
        "description": "Minimalist travel wardrobe guide. Build a 10-piece capsule that "
                       "works for 2 weeks anywhere — packing light without sacrificing style. "
                       "Includes brand recommendations and outfit formulas.",
        "price_cents": 399,   # €3.99
    },
    {
        "key":         "visa",
        "name":        "UncleMarv Visa Check",
        "description": "Visa & entry requirements cheat sheet. Country-by-country breakdown "
                       "of visa requirements, processing times, e-visa portals and border "
                       "tips. Never get caught out at immigration.",
        "price_cents": 599,   # €5.99
    },
    {
        "key":         "photoposes",
        "name":        "UncleMarv Lens Guide",
        "description": "Travel photography poses & shot guide. 60+ photo ideas with "
                       "composition tips, lighting notes and location scouting advice. "
                       "Level up your travel feed — no professional camera required.",
        "price_cents": 699,   # €6.99
    },
    {
        "key":         "bundle",
        "name":        "UncleMarv Complete",
        "description": "The full UncleMarv bundle. All 9 digital products in one discounted "
                       "package — wallpapers, LUTs, presets, guides, checklists and more. "
                       "Best value for the serious traveller.",
        "price_cents": 3499,  # €34.99
    },
]

# ─── API-Hilfsfunktionen ────────────────────────────────────────────────────
BASE_URL = "https://api.lemonsqueezy.com/v1"

def api(method, path, api_key, data=None):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.api+json",
        "Content-Type": "application/vnd.api+json",
    }
    url = f"{BASE_URL}{path}"
    resp = requests.request(method, url, headers=headers,
                            json=data if data else None, timeout=30)
    if not resp.ok:
        print(f"  ✗ HTTP {resp.status_code}: {resp.text[:300]}")
        return None
    return resp.json()

def get_store_id(api_key):
    data = api("GET", "/stores", api_key)
    if not data or not data.get("data"):
        print("Kein Store gefunden. Bitte zuerst einen Store anlegen.")
        sys.exit(1)
    store = data["data"][0]
    sid = store["id"]
    slug = store["attributes"]["slug"]
    print(f"  ✓ Store gefunden: {slug} (ID: {sid})")
    return sid, slug

def create_product(api_key, store_id, product):
    payload = {
        "data": {
            "type": "products",
            "attributes": {
                "name":        product["name"],
                "description": product["description"],
            },
            "relationships": {
                "store": {
                    "data": {"type": "stores", "id": str(store_id)}
                }
            }
        }
    }
    resp = api("POST", "/products", api_key, payload)
    if not resp:
        return None
    return resp["data"]["id"]

def create_variant(api_key, product_id, product):
    payload = {
        "data": {
            "type": "variants",
            "attributes": {
                "name":        "Standard",
                "price":       product["price_cents"],
                "is_subscription": False,
                "has_free_trial": False,
            },
            "relationships": {
                "product": {
                    "data": {"type": "products", "id": str(product_id)}
                }
            }
        }
    }
    resp = api("POST", "/variants", api_key, payload)
    if not resp:
        return None
    return resp["data"]["id"]

# ─── Hauptprogramm ──────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    api_key = sys.argv[1].strip()
    print("\n🚀 UncleMarv — LemonSqueezy Setup\n" + "─"*40)

    # Store-ID holen
    print("\n① Store laden …")
    store_id, store_slug = get_store_id(api_key)

    results = {}
    print(f"\n② Produkte erstellen …\n")

    for p in PRODUCTS:
        print(f"  → {p['name']} (€{p['price_cents']/100:.2f})")

        # Produkt anlegen
        pid = create_product(api_key, store_id, p)
        if not pid:
            print(f"     ✗ Produkt konnte nicht erstellt werden")
            continue

        # Variante anlegen
        time.sleep(0.5)  # Rate-limit schonen
        vid = create_variant(api_key, pid, p)
        if not vid:
            print(f"     ✗ Variante konnte nicht erstellt werden")
            continue

        checkout_url = f"https://{store_slug}.lemonsqueezy.com/buy/{vid}"
        results[p["key"]] = checkout_url
        print(f"     ✓ {checkout_url}")
        time.sleep(0.3)

    # Ergebnisse speichern
    output_file = "ls_urls.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n✅ Fertig! URLs gespeichert in: {output_file}")

    # JS-Patch-Code ausgeben
    print("\n─── Kopiere diesen Block in index.html (PRODUCTS-Objekt) ───")
    for key, url in results.items():
        prod_info = next((p for p in PRODUCTS if p["key"] == key), None)
        if prod_info:
            cents = prod_info["price_cents"]
            name  = prod_info["name"]
            price = cents / 100
            print(f'    {key+":":12} {{ name: {repr(name):30}, price: {price:5.2f}, img: \'\', lsUrl: {repr(url)} }},')

    print("─"*60)

if __name__ == "__main__":
    main()
