gaji = int(input("Penghasilan per bulan: "))
pekerjaan = input("Jenis pekerjaan (pns/non-pns): ")
pajak = 0

if gaji >= 5000000:
    pajak = 10/100 * gaji
elif gaji >= 3000000:
    pajak = 5/100 * gaji
else:
	print("Tidak ada pajak Umum")

if pekerjaan == "pns":
    pajak += 5/100 * gaji
else:
	print("Tidak ada pajak PNS")

bersih = gaji - pajak
print("Penghasilan bersih per bulan: ",bersih)