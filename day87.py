def prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
    return True

print("Masukkan bilangan: ")
bilangan = int(input())

if prima(bilangan):
    print("Bilangan {} adalah bilangan prima.".format(bilangan))
else:
    print("Bilangan {} bukan bilangan prima.".format(bilangan))
