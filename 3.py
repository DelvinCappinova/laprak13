def jumlah(n):
    if n == 1:
        return 1
    return jumlah(n-1) + (2*n - 1)

n = 5
print(f"Jumlah deret ganjil hingga bilangan ke-{n} adalah {jumlah(n)}")