def brojac_unatrag(n, m, k):
    if n <= m:
        return m
    else:
        print(n)
        return brojac_unatrag(n - k, m, k)

while True:    
    x = input('Unesite broj: ')
    k = input('Unesite korak: ')
    print(x, k)
    if x.isdigit() == True and k.isdigit() == True:
        print(brojac_unatrag(int(x), -(int(x)), int(k)))
        break
    elif x.isdecimal() == True or k.isdecimal() == True:
        print(brojac_unatrag(float(x), -(float(x)), float(k)))
        break
    else:
        continue