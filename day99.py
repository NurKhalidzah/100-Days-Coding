def aritmatika(angka):
    for i in range(1, angka + 1):
        if i % 2 == 0:
            print(f"{i} adalah bilangan genap.")
        else:
            if i % 3 == 0:
                print(f"{i} adalah kelipatan 3.")
            elif i % 5 == 0:
                print(f"{i} adalah kelipatan 5.")
            else:
                print(f"{i} bukan bilangan genap, bukan kelipatan 3, dan bukan kelipatan 5.")

nilai = int(input("Masukkan Angka: "))
aritmatika(nilai)