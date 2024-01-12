# Fungsi untuk menghitung faktorial
def faktorial(n):
    if n == 0:
        return 1
    return n * faktorial(n - 1)

# Fungsi untuk menghitung jumlah angka prima di dalam suatu bilangan
def jumlah_angka_prima(n):
    if n <= 1:
        return 0

    jumlah = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0

    jumlah += 1
    if n % 2 == 0 and n != 2:
        jumlah += 1

    return jumlah

# Fungsi untuk menghitung jumlah solusi dari persamaan kuadrat
def jumlah_solusi_kuadrat(a, b, c):
    if a == 0:
        if b == 0:
            return 0
        else:
            return 1

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return 0
    elif delta == 0:
        return 1
    else:
        return 2

# Mengambil input dari pengguna
angka = int(input("Masukkan bilangan: "))
b = int(input("Masukkan nilai b: "))
c = int(input("Masukkan nilai c: "))
# Menghitung faktorial dari angka yang dimasukkan
print("Faktorial dari ", angka, "adalah", faktorial(angka))

# Menghitung jumlah angka prima di dalam angka yang dimasukkan
print("Jumlah angka prima di dalam ", angka, "adalah", jumlah_angka_prima(angka))

# Menghitung jumlah solusi dari persamaan kuadrat dengan koefisien a, b, dan c yang dimasukkan
print("Jumlah solusi dari persamaan kuadrat x^2 + ", b, "x + ", c, "adalah", jumlah_solusi_kuadrat(1, b, c))


