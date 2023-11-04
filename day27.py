def hitung_keliling_segitiga(sisi1, sisi2, sisi3):
    keliling = sisi1 + sisi2 + sisi3
    return keliling
sisi1 = int(input("sisi 1: "))
sisi2 = int(input("sisi 2: "))
sisi3 = int(input("sisi 3: "))
keliling = hitung_keliling_segitiga(sisi1, sisi2, sisi3)
print("Keliling segitiga:", keliling)