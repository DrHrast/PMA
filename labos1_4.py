while True:
    a = int(input('unesite broj: '))
    for i in range (10):
        rez = a*(i+1)
        if a > 400 or rez > 400:
            break
        print(f'{a} X {i + 1} = {a*(i+1)}')