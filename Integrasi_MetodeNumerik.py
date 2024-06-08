import time
import numpy as np

def f(x):
    return 4 / (1 + x**2)

def riemann(a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        x = a + i * h
        integral += f(x)
    integral *= h
    return integral


# Batas integral
a = 0
b = 1

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi N (jumlah segmen)
N_values = [10, 100, 1000, 10000]

# Menyimpan hasil
results_riemann = []
results_simpson = []

for n in N_values:
    # Riemann
    start_time = time.time()
    pi_approx_riemann = riemann(a, b, n)
    end_time = time.time()
    
    # Menghitung galat RMS
    rms_error_riemann = np.sqrt((pi_approx_riemann - pi_reference)**2)
    
    # Mengukur waktu eksekusi
    execution_time_riemann = end_time - start_time
    
    results_riemann.append((n, pi_approx_riemann, rms_error_riemann, execution_time_riemann))


# Menampilkan hasil
print("Metode Riemann")
print(f"{'N':>10} {'Pi Approximation':>20} {'RMS Error':>20} {'Execution Time (s)':>20}")
for result in results_riemann:
    print(f"{result[0]:>10} {result[1]:>20.15f} {result[2]:>20.15f} {result[3]:>20.15f}")

