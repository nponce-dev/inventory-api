import pandas as pd
import requests
import re

API = "https://inventory-api-production-6d9d.up.railway.app"
EXCEL_FILE = "Stock.xlsx"
USERNAME = "admin"
PASSWORD = "1244" 

def get_token():
    res = requests.post(f"{API}/token", data={"username": USERNAME, "password": PASSWORD})
    return res.json()["access_token"]

def make_sku(producto, tamano):
    base = str(producto).strip().upper()
    base = re.sub(r'\s+', '-', base)
    base = re.sub(r'[^A-Z0-9\-]', '', base)
    if pd.notna(tamano) and str(tamano).strip():
        suffix = re.sub(r'\s+', '', str(tamano).strip().upper())
        return f"{base}-{suffix}"
    return base

token = get_token()
headers = {"Authorization": f"Bearer {token}"}

df = pd.read_excel(EXCEL_FILE, sheet_name="Hoja1")
df.columns = [c.strip() for c in df.columns]

ok = 0
errores = []

for _, row in df.iterrows():
    nombre = str(row["PRODUCTO"]).strip()
    stock = int(row["STOCK"]) if pd.notna(row["STOCK"]) else 0
    sku = make_sku(row["PRODUCTO"], row.get("TAMANO"))

    payload = {"name": nombre, "sku": sku, "stock": stock}

    try:
        res = requests.post(f"{API}/products/", json=payload, headers=headers)
        if res.status_code == 200:
            print(f"  ✓ {nombre} ({sku}) — stock: {stock}")
            ok += 1
        else:
            msg = res.json().get("detail", res.text)
            print(f"  ✗ {nombre} ({sku}) — {msg}")
            errores.append(nombre)
    except Exception as e:
        print(f"  ✗ {nombre} — error de conexión: {e}")
        errores.append(nombre)

print(f"\n{ok} productos importados correctamente.")
if errores:
    print(f"{len(errores)} con error: {errores}")