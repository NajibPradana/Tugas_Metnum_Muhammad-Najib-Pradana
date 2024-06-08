import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# X = Jumlah Latihan Soal
# Y = Nilai Ujian
latihan = np.array([1, 2, 2, 2, 5, 6, 6, 6, 2, 0])
nilai = np.array([91, 65, 45, 36, 66, 61, 63, 42, 61, 69])

# Fungsi untuk Regresi Linear (Metode 1)
def regresi_linear(x, a, b):
    return a + b * x

# Fungsi untuk Model Pangkat Sederhana (Metode 2)
def model_pangkat(x, a, b):
    return a * x ** b

# Plot titik data
plt.figure(figsize=(12, 6))

# Plot untuk Regresi Linear (Metode 1)
plt.subplot(1, 2, 1)
plt.scatter(latihan, nilai, color='blue', label='Data')
rata_latihan = np.mean(latihan)
rata_nilai = np.mean(nilai)
b_linear = np.sum((latihan - rata_latihan) * (nilai - rata_nilai)) / np.sum((latihan - rata_latihan)**2)
a_linear = rata_nilai - b_linear * rata_latihan
x_linear = np.linspace(min(latihan), max(latihan), 100)
y_linear = regresi_linear(x_linear, a_linear, b_linear)
plt.plot(x_linear, y_linear, color='red', label='Regresi Linear')
plt.title('Model Linear (Metode 1)')
plt.xlabel('Jumlah Latihan')
plt.ylabel('Nilai Ujian')
plt.legend()
plt.grid(True)

# Plot untuk Model Pangkat Sederhana (Metode 2)
plt.subplot(1, 2, 2)
plt.scatter(latihan, nilai, color='blue', label='Data')
popt_pangkat, _ = curve_fit(model_pangkat, latihan[latihan > 0], nilai[latihan > 0], p0=(1, 1))
x_pangkat = np.linspace(min(latihan[latihan > 0]), max(latihan), 100)
y_pangkat = model_pangkat(x_pangkat, *popt_pangkat)
plt.plot(x_pangkat, y_pangkat, color='green', label='Model Pangkat Sederhana')
plt.title('Model Pangkat Sederhana (Metode 2)')
plt.xlabel('Jumlah Latihan')
plt.ylabel('Nilai Ujian')
plt.legend()
plt.grid(True)

# Tampilkan plot
plt.tight_layout()
plt.show()

# Menghitung galat RMS untuk Regresi Linear (Metode 1)
prediksi_linear = regresi_linear(latihan, a_linear, b_linear)
rms_galat_linear = np.sqrt(np.mean((nilai - prediksi_linear)**2))
print("Galat RMS (Linear): ", rms_galat_linear)

# Menghitung galat RMS untuk Model Pangkat Sederhana (Metode 2)
prediksi_pangkat = model_pangkat(latihan[latihan > 0], *popt_pangkat)
rms_galat_pangkat = np.sqrt(np.mean((nilai[latihan > 0] - prediksi_pangkat)**2))
print("Galat RMS (Pangkat Sederhana): ", rms_galat_pangkat)
