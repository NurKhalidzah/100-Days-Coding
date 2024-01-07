tinggi_segitiga = int(input('Input tinggi segitiga: '))
print()
 
for i in range(1,tinggi_segitiga+1):
  for j in range(tinggi_segitiga-i+1):
    print(i,' ',end='',sep='')
  print()