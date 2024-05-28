def palindrom(s):

    s = ''.join(c.lower() for c in s if c.isalnum())
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])

kalimat = input("Masukkan kalimat: ")
if palindrom(kalimat):
    print(f'"{kalimat}" adalah palindrom.')
else:
    print(f'"{kalimat}" bukan palindrom.')