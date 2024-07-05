def aturan_trapesium(f, a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]
    
    integral = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return integral

# Definisikan fungsi yang akan diintegrasikan
def fungsi(x):
    return 2.718281828459045 ** x  # Pendekatan dari e^x
# digunakan sebagai fungsi yang akan diintegrasikan dalam metode aturan trapesium

# Perhitungan nilai integral sebenarnya
def integral_sebenarnya(a, b):
    e = 2.718281828459045  
    # e dalam fungsi integral_sebenarnya diambil sebagai pendekatan dari bilangan Euler, 
    # yang merupakan dasar dari logaritma natural dan memiliki nilai sekitar 2.718281828459045
    return e ** b - e ** a


a = float(input("Masukan nilai a :"))
b = float(input("Masukan nilai b :"))
n = int(input("Masukan nilai n :"))  # Ini diambil dari gambar di mana ada 8 segmen (h = 0.2)

# Hitung integral pendekatan
integral_pendekatan = aturan_trapesium(fungsi, a, b, n)

# Hitung nilai integral sebenarnya
nilai_integral_sebenarnya = integral_sebenarnya(a, b)

# Galat kaidah trapesium
galatKaidahTrapesium = nilai_integral_sebenarnya - integral_pendekatan

print(f"Nilai integral metodenya : {integral_pendekatan:.6f}")
print(f"Nilai integral sejatinya: {nilai_integral_sebenarnya:.6f}")
print(f"Nilai galat kaidah trapesiumnya adalah : {galatKaidahTrapesium:.6f}")
