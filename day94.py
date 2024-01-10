def pecah_bilangan(n):

  faktor = []

  for i in range(2, int(n ** 0.5) + 1):
    if is_prime(i):
      while n % i == 0:
        faktor.append(i)
        n //= i

  if n > 1:
    if is_prime(n):
      faktor.append(n)

  return faktor

def is_prime(n):

  if n < 2:
    return False

  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False

  return True

bilangan = int(input("Masukkan bilangan: "))
faktor = pecah_bilangan(bilangan)  # Pass bilangan to the function

print("Faktor-faktor prima dari", bilangan, "adalah:")
for f in sorted(faktor):
    print(f, end=" ")

