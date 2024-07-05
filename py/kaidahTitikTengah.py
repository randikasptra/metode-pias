def titik_tengah(a, b, n):
    h = (b - a) / n  # lebar pias
    x = a + h / 2  # titik tengah pertama
    sigma = f(x)
    
    for r in range(1, n):
        x += h
        sigma += f(x)
        
    I = sigma * h  # nilai integrasi numerik
    return I

# Definisikan fungsi f(x) yang akan diintegrasikan
def f(x):
    return 2.718281828459045 ** x  # pendekatan dari e^x

# Input nilai a, b, dan n
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
n = int(input("Masukkan jumlah pias (n): "))

# Hitung nilai integral pendekatan
integral_pendekatan = titik_tengah(a, b, n)

# Tampilkan hasil
print(f"Nilai integral metodenya: {integral_pendekatan:.6f}")
