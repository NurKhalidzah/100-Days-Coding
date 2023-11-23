print("[1].Samsung")
print("[2].Vivo")
print("[3].iPhone")
diskon = 0
harga = 0
merek = input("pilih merek HP: ")
if merek == "1":
    print("[1].Samsung Galaxy Fold 5","\nRp.24900000")
    print("[2].Samsung Galaxy Flip","\nRp.15900000")
    tipe = input("Pilih Tipe HP: ")
    if tipe == "1":
        kartu = input("Kartu Member/Tidak: ")
        if kartu == "Kartu Member":
            print("Anda mendapatkan Diskon 5%")
            diskon = 24900000 * 5/100
        else:
            print("Tidak Mendapat Diskon")
        kode = input("ketik kode diskon: ")
        if kode == "yeeediskon":
            print("Anda mendapatkan Diskon 5%")
            diskon +=5/100 * 24900000
        else:
            print("Tidak Mendapat Diskon")
        total = 24900000 - diskon
        print("Total Harga:",total)
    
    if tipe == "2":
        kartu = input("Kartu Member/Tidak: ")
        if kartu == "Kartu Member":
            print("Anda mendapatkan Diskon 5%")
            diskon = 15900000 * 5/100
        else:
            print("Tidak Mendapat Diskon")
        kode = input("ketik kode diskon: ")
        if kode == "yeeediskon":
            print("Anda mendapatkan Diskon 5%")
            diskon +=5/100 * 15900000
        else:
            print("Tidak Mendapat Diskon")
        total = 15900000 -diskon
        print("Total Harga:",total)
        
if merek == "2":
    print("[1].Vivo V29 5G","\nRp.6999000")
    print("[2].Vivo Y36 5G","\nRp.3499000")
    tipe = input("Pilih Tipe HP: ")
    if tipe == "1":
        kartu = input("Kartu Member/Tidak: ")
        if kartu == "Kartu Member":
            print("Anda mendapatkan Diskon 5%")
            diskon = 6999000 * 5/100
        else:
            print("Tidak Mendapat Diskon")
        kode = input("ketik kode diskon: ")
        if kode == "yeeediskon":
            print("Anda mendapatkan Diskon 5%")
            diskon +=5/100 * 6999000
        else:
            print("Tidak Mendapat Diskon")
        total = 6999000 - diskon
        print("Total Harga:",total)

    if tipe == "2":
        kartu = input("Kartu Member/Tidak: ")
        if kartu == "Kartu Member":
            print("Anda mendapatkan Diskon 5%")
            diskon = 3499000 * 5/100
        else:
            print("Tidak Mendapat Diskon")
        kode = input("ketik kode diskon: ")
        if kode == "yeeediskon":
            print("Anda mendapatkan Diskon 5%")
            diskon +=5/100 * 3499000
        else:
            print("Tidak Mendapat Diskon")
        total = 3499000 - diskon
        print("Total Harga:",total)

if merek == "3":
    print("[1].iphone 15 Pro Max","\nRp.3500000")
    print("[2].iphone 14 Pro Max","\nRp.3300000")
    tipe = input("Pilih Tipe HP: ")
    if tipe == "1":
        kartu = input("Kartu Member/Tidak: ")
        if kartu == "Kartu Member":
            print("Anda mendapatkan Diskon 5%")
            diskon = 3500000 * 5/100
        else:
            print("Tidak Mendapat Diskon")
        kode = input("ketik kode diskon: ")
        if kode == "yeeediskon":
            print("Anda mendapatkan Diskon 5%")
            diskon +=5/100 * 3500000
        else:
            print("Tidak Mendapat Diskon")
        total = 3500000 - diskon
        print("Total Harga:",total)
    if tipe == "2":
        kartu = input("Kartu Member/Tidak: ")
        if kartu == "Kartu Member":
            print("Anda mendapatkan Diskon 5%")
            diskon = 3300000 * 5/100
        else:
            print("Tidak Mendapat Diskon")
        kode = input("ketik kode diskon: ")
        if kode == "yeeediskon":
            print("Anda mendapatkan Diskon 5%")
            diskon +=5/100 * 3300000
        else:
            print("Tidak Mendapat Diskon")
        total = 3300000 - diskon
        print("Total Harga:",total)
        
         
     

        
        
  
  
