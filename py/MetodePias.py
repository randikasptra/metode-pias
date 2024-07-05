import math

# Fungsi yang akan diintegrasikan (e^x)
def fungsi(x):
    return math.exp(x)

# Aturan Trapesium
def aturan_trapesium(f, a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]
    integral = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return integral

# Kaidah Titik Tengah
def titik_tengah(f, a, b, n):
    h = (b - a) / n
    x = a + h / 2
    sigma = f(x)
    for r in range(1, n):
        x += h
        sigma += f(x)
    I = sigma * h
    return I

# Kaidah Segi Empat (Rectangle Rule)
def metode_pias_kaidah_segiempat(f, a, b, n):
    h = (b - a) / n
    total = 0
    for i in range(1, n + 1):
        x_i = a + h * (i - 1)
        f_i = f(x_i)
        total += f_i
    integral = h * total
    return integral

# Fungsi utama untuk menjalankan program
def main():
    a = float(input("Masukkan batas bawah integrasi (a): "))
    b = float(input("Masukkan batas atas integrasi (b): "))
    n = int(input("Masukkan jumlah pias (n): "))

    # Hitung integral menggunakan aturan trapesium
    integral_trapesium = aturan_trapesium(fungsi, a, b, n)
    print(f"Nilai integral metode trapesium: {integral_trapesium:.6f}")

    # Hitung integral menggunakan kaidah titik tengah
    integral_titik_tengah = titik_tengah(fungsi, a, b, n)
    print(f"Nilai integral metode titik tengah: {integral_titik_tengah:.6f}")

    # Hitung integral menggunakan kaidah segi empat
    integral_segi_empat = metode_pias_kaidah_segiempat(fungsi, a, b, n)
    print(f"Nilai integral metode segi empat: {integral_segi_empat:.6f}")

if __name__ == "__main__":
    main()