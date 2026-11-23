import pandas as pd

# 1. Input & Pembacaan Data
df = pd.read_csv("Persentase_Cakupan_Ketersediaan_Rumah_Layak_Huni.csv.csv")
print(df.shape)
print(df.head())

# 2. Pembersihan Data
# Penyesuaian dataset: kolom tahun masih teks ("-" dan koma desimal), diubah ke angka
for kolom in ["Tahun 2022", "Tahun 2023"]:
    df[kolom] = df[kolom].astype(str).str.replace(",", ".", regex=False)
    df[kolom] = pd.to_numeric(df[kolom], errors="coerce")

print(df.isna().sum())
df["Indikator"] = df["Indikator"].str.strip()
df["Satuan"] = df["Satuan"].str.strip()
df = df.drop_duplicates()
print(df.describe())

df.to_csv("rumah_bersih.csv", index=False)