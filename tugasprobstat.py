import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# ===============================
# 1️⃣ Baca data CSV
# ===============================
df = pd.read_csv("C:\\Users\\INTAN\\Downloads\\Jumlah Pasar Menurut Potensi Pasar (Maju), 2009-2013.csv", skiprows=2)

# Bersihkan nama kolom dari spasi
df.columns = df.columns.str.strip()

# Ambil kolom Wilayah dan 2009
data_2009 = df[["Wilayah", "2009"]].copy()

# Bersihkan nilai kolom 2009 agar menjadi angka
data_2009 = data_2009.dropna()
data_2009["2009"] = data_2009["2009"].astype(str).str.replace(r"\D", "", regex=True)
data_2009["2009"] = data_2009["2009"].replace("", 0).astype(int)

# ===============================
# 2️⃣ Hitung statistik deskriptif
# ===============================
mean_2009 = data_2009["2009"].mean()
median_2009 = data_2009["2009"].median()
mode_2009 = data_2009["2009"].mode()[0]
variance_2009 = data_2009["2009"].var()
std_dev_2009 = data_2009["2009"].std()

# Cetak hasil
print("\n📊 Statistik Tahun 2009:")
print(f"Mean: {mean_2009:.2f}")
print(f"Median: {median_2009}")
print(f"Mode: {mode_2009}")
print(f"Variance: {variance_2009:.2f}")
print(f"Standard Deviation: {std_dev_2009:.2f}")

# ===============================
# 3️⃣ Buat histogram & kurva kontinu
# ===============================

# Siapkan data numerik
x = data_2009["2009"]

# Hitung kernel density (agar kurvanya halus)
kde = gaussian_kde(x)
x_grid = np.linspace(x.min(), x.max(), 200)
kde_values = kde(x_grid)

# Buat histogram
plt.figure(figsize=(8,5))
plt.hist(
    x, bins=10, density=True,
    alpha=0.4, color="skyblue",
    edgecolor="black", label="Histogram"
)

# Tambahkan garis kontinu (kurva KDE)
plt.plot(x_grid, kde_values, color="blue", linewidth=2, label="Kurva Kontinu")

# Tambahkan garis vertikal mean, median, mode
plt.axvline(mean_2009, color='red', linestyle='--', label=f'Mean: {mean_2009:.2f}')
plt.axvline(median_2009, color='green', linestyle='--', label=f'Median: {median_2009}')
plt.axvline(mode_2009, color='orange', linestyle='--', label=f'Mode: {mode_2009}')

# ===============================
# 4️⃣ Hias grafik
# ===============================
plt.title("Histogram Jumlah Pasar Tahun 2009 (Grafik Kontinu)")
plt.xlabel("Jumlah Pasar (2009)")
plt.ylabel("Frekuensi Relatif (Density)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
