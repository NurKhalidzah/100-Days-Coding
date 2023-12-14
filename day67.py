gaji = int(input("penghasilan: "))
batas = 5240000
zakat = 0

if gaji >= batas:
  besaran = (2.5/100)*gaji
  zakat = besaran

bersih = gaji - zakat

print("zakat: ", zakat)
print("bersih: ", bersih)