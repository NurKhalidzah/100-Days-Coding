a = int(input("angka 1: "))
b = int(input("angka 2: "))
total = 0
output = ""

for i in range(a, b+ 1):
    total += i
    output += str(i)
    if i < b:
        output += "+"

output += " = " + str(total)
print(output)