def genap_ganjil(a, b):
 
  hasil = a + b
  if hasil % 2 == 0:
    return "Genap"
  else:
    return "Ganjil"
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
print(f"Hasil penjumlahan {a} + {b} adalah {a + b}.")
print(f"{a + b} adalah bilangan {genap_ganjil(a, b)}.")
