def is_genap(x):
  return x % 2 == 0

def is_prima(x):
  if x <= 1:
    return False
  for i in range(2, int(x ** 0.5) + 1):
    if x % i == 0:
      return False
  return True

def main():
  a = int(input("Masukkan angka pertama: "))
  b = int(input("Masukkan angka kedua: "))

  penjumlahan = a + b

  print("Hasil penjumlahan:", penjumlahan)

  if is_genap(penjumlahan):
    print("Bilangan genap")
  else:
    print("Bilangan ganjil")

  if is_prima(penjumlahan):
    print("Bilangan prima")
  else:
    print("Bukan bilangan prima")

if __name__ == "__main__":
  main()
