import pandas as pd

CSV_PATH = "products.csv"
XLSX_PATH = "products.xlsx"

COLUMN_MAPPING = {
    "Item Id": "id",
    "Item Name": "title",
    "Price": "price",
    "Offer Link": "affiliate_url",
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
]

df_raw = pd.read_csv(CSV_PATH, encoding="utf-8-sig")

df = pd.DataFrame()

for src, dest in COLUMN_MAPPING.items():
    if src in df_raw.columns:
        df[dest] = df_raw[src]

for col in FINAL_COLUMNS:
    if col not in df.columns:
        df[col] = ""

df["active"] = True

df = df[FINAL_COLUMNS]

df.to_excel(XLSX_PATH, index=False)

print("✅ XLSX gerado com sucesso com schema padronizado")