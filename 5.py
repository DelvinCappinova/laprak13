def kombin(n, k):
    if k == 0 or k == n:
        return 1
    return kombin(n-1, k-1) + kombin(n-1, k)
n = 5
k = 2
print(f"C({n}, {k}) = {kombin(n, k)}")