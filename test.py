import pandas as pd

df = pd.read_csv("Persentase_Cakupan_Ketersediaan_Rumah_Layak_Huni.csv.csv")
print(df.shape)
print(df.head())
print(df.info())

# 1. Buang kolom yang tidak dipakai
df = df.drop(columns=["_full_text", "_id"])

# 2. Ganti koma desimal jadi titik, lalu ubah ke angka
for kolom in ["Tahun 2022", "Tahun 2023"]:
    df[kolom] = df[kolom].astype(str).str.replace(",", ".", regex=False)
    df[kolom] = pd.to_numeric(df[kolom], errors="coerce")

# 3. Rapikan teks
for kolom in ["Indikator", "Satuan"]:
    df[kolom] = df[kolom].str.strip()

print(df.isna().sum())   # cek dulu: Tahun 2022 = 3 (kosong semua)

# 4. Hapus kolom yang kosong semua
df = df.drop(columns=["Tahun 2022"])

print(df.dtypes)
print(df)

df.to_csv("rumah_bersih.csv", index=False)

print(df.isna().sum())
print(df.dtypes)
print(df)

