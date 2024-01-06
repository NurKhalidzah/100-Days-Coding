
def hitung_luas_segitiga(alas, tinggi):
    
    return (alas * tinggi) / 2

def hitung_luas_persegi(sisi):
    
    return sisi * sisi

def hitung_luas_persegi_panjang(panjang, lebar):
    
    return panjang * lebar

print("Masukkan bentuk: ")
bentuk = input()

if bentuk == "segitiga":
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = hitung_luas_segitiga(alas, tinggi)
    print("Luas dari bentuk", bentuk, "adalah", luas)
elif bentuk == "persegi":
    sisi = float(input("Masukkan sisi persegi: "))
    luas = hitung_luas_persegi(sisi)
    print("Luas dari bentuk", bentuk, "adalah", luas)
elif bentuk == "persegi_panjang":
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    luas = hitung_luas_persegi_panjang(panjang, lebar)
    print("Luas dari bentuk", bentuk, "adalah", luas)
else:
    print("Bentuk yang Anda masukkan tidak valid.")