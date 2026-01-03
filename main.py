import pandas as pd

CSV_PATH = "products.csv"
XLSX_PATH = "products.xlsx"

COLUMN_MAPPING = {
    "Item Id": "id",
    "Item Name": "title",
    "Price": "price",
    "Offer Link": "affiliate_url",
    "Sales": "sales",
    "Commission": "commission"
}

FINAL_COLUMNS = [
    "id",
    "title",
    "price",
    "original_price",
    "discount_percentage",
    "image_url",
    "affiliate_url",
    "category",
    "active",
    "sales",
    "commission"
]

DEFAULTS = {
    "original_price": 0.0,
    "discount_percentage": 0.0,
    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtvTrKGonpRbf05O2HlzZxhiszSSmwMww0Z8c3esRYsQ&s",
    "category": "Genérico",
    "active": "TRUE",
}

df_raw = pd.read_csv(CSV_PATH, encoding="utf-8-sig", dtype=str)

df = pd.DataFrame()

for src, dest in COLUMN_MAPPING.items():
    if src in df_raw.columns:
        df[dest] = df_raw[src]

if "price" in df.columns:
    df["price"] = (
        df["price"]
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

for col in FINAL_COLUMNS:
    if col not in df.columns:
        df[col] = DEFAULTS.get(col, "")

for col, value in DEFAULTS.items():
    df[col] = df[col].fillna(value)

df = df[FINAL_COLUMNS]

df.to_excel(XLSX_PATH, index=False)

print("✅ XLSX gerado")
