def sum(n):
    if n == 0:
        return 0
    return n % 10 + sum(n // 10)

bilangan = 234
print(f"Jumlah digit dari {bilangan} adalah {sum(bilangan)}")