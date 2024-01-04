def cek_hari(tanggal):
    if tanggal % 7 == 0:
        return "Minggu"
    elif tanggal % 7 == 1:
        return "Senin"
    elif tanggal % 7 == 2:
        return "Selasa"
    elif tanggal % 7 == 3:
        return "Rabu"
    elif tanggal % 7 == 4:
        return "Kamis"
    elif tanggal % 7 == 5:
        return "Jumat"
    else:
        return "Sabtu"


def main():
    tanggal = int(input("Masukkan tanggal: "))
    hari = cek_hari(tanggal)
    print(f"Tanggal {tanggal} adalah {hari}")


if __name__ == "__main__":
    main()
