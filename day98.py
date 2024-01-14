def cek_logika_aritmetika(angka):
    for i in range(1, angka + 1):
        if i % 2 == 0 and i % 3 == 0:
            print(f"{i} adalah kelipatan 2 dan 3")
        elif i % 2 == 0:
            print(f"{i} adalah kelipatan 2")
        elif i % 3 == 0:
            print(f"{i} adalah kelipatan 3")
        else:
            print(f"{i} bukan kelipatan 2 atau 3")
input_angka = int(input("Masukkan angka: "))
cek_logika_aritmetika(input_angka)