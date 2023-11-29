panjang = int(input("panjang: "))
genap  = []
ganjil = []
for i in range(panjang):
    nilai = int(input("nilai: "))
    if nilai %2 == 0:
        genap.append(nilai)
    else:
        ganjil.append(nilai)
for j in range(0, len(genap)):
    print("genap: ",genap[j])
for k in range(0, len(ganjil)):
    print("ganjil: ",ganjil[k])
               
    
    
