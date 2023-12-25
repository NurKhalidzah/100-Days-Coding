batas = int(input("masukkan batas: "))
arr = []
jumlah = 0

for i in range( batas):
    isi = int(input("masukkan angka: "))
    arr.append(isi)
    jumlah += isi
rataRata = jumlah / (batas - 1)
print("Rata-rata: ",rataRata)