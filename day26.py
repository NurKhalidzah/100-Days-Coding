while True:
    a = int(input("Masukkan nilai a: "))
    b = int(input("Masukkan nilai b: "))
    
    if a < b:
        for i in range(a, b + 1 ):
            print(i)
    else:
        for i in range(b, a + 1):
            print(i)