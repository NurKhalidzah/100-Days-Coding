a = int(input("angka 1: "))
b = int(input("angka 2: "))
hasil = a + b
if hasil %2 == 0:
	hasil +=2
	print("genap: ",hasil)
else:
	hasil +=1
	print("ganjil: ",hasil)