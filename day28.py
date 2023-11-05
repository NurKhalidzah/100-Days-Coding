def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b
    
def bagi(a, b):
    if b and a == 0:
    	return("Pembagian Nol tidak di bolehkan")
    return a / b

angka1 = int(input("angka 1: "))
angka2 = int(input("angka 2: "))

hasil_penambahan = tambah(angka1, angka2)
hasil_pengurangan = kurang(angka1, angka2)
hasil_perkalian = kali(angka1, angka2)
hasil_pembagian = bagi(angka1, angka2)

print("Hasil Penambahan:", hasil_penambahan)
print("Hasil Pengurangan:", hasil_pengurangan)
print("Hasil Perkalian:", hasil_perkalian)
print("Hasil Pembagian:", hasil_pembagian)