#if else (Diskon)
total_belanja = int(input("Masukkan total belanja Anda: "))

if total_belanja >= 100000:
    diskon = total_belanja * (25/100)
    Total_harga = total_belanja - diskon
    print("Anda mendapat Diskon sebesar 25% ")
    print("Total Harga Belanja Anda: ",Total_harga)
else:
    print("Anda tidak mendapat Diskon")
    print("Total Harga Belanja Anda: ",total_belanja)

                    
