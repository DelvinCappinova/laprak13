def rekursif(n, pembagi=2):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % pembagi == 0:
        return False
    if pembagi * pembagi > n:
        return True
    return rekursif(n, pembagi + 1)

bilangan = int(input("Masukkan bilangan: "))
if rekursif(bilangan):
    print(f"{bilangan} adalah bilangan prima.")
else:
    print(f"{bilangan} bukan bilangan prima.")