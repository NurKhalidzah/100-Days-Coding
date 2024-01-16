def aritmatika(angka):
    if angka < 2:
        return False
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            return False
    return True

n = int(input("Masukkan sebuah bilangan positif: "))
if n > 0:
    print(f"{n} {'adalah' if aritmatika(n) else 'bukan'} bilangan prima.")
else:
    print("Masukkan bilangan positif yang lebih dari 0.")