def metode_pias_kaidah_segiempat(a, b, n):
  h = (b - a) / n
  total = 0

  # Menghitung nilai di setiap titik
  for i in range(1, n + 1):
    x_i = a + h * (i - 1)
    f_i = hitung_fungsi(x_i)  # Ganti dengan fungsi yang ingin diintegrasikan

    if i == 1 or i == n:
      total += f_i / 2  # Menangani kasus ujung
    else:
      total += f_i

  # Menghitung integral
  integral = (h / 6) * total
  return integral

def hitung_fungsi(x):
  return x**2

# Menginput nilai dari user
a = float(input("Masukkan batas bawah integrasi (a): "))
b = float(input("Masukkan batas atas integrasi (b): "))
n = int(input("Masukkan jumlah segiempat (n): "))

# Menghitung dan menampilkan integral
integral = metode_pias_kaidah_segiempat(a, b, n)
print(f"Nilai integral: {integral}")
