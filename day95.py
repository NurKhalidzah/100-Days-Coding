def hitung_rumus(a, b, c):

  return a**3 + b**2 - c


a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))


if hitung_rumus(a, b, c) >= 0:
  print("Hasil rumus:", hitung_rumus(a, b, c))
else:
  print("Hasil rumus:", -hitung_rumus(a, b, c))
