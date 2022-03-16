while True:
    godina = int(input('Upisite neku godinu: '))
    if godina > 1584:
        if godina % 4 == 0:
            if godina % 100 != 0:
                print(f'Godina {godina} je prijestupna.')
                break
            elif godina % 100 == 0 and godina % 400 == 0:
                print(f'Godina {godina} je prijestupna.')
                break
            else:
                print(f'Godina {godina} nije prijestupna')
        else:
            print(f'Godina {godina} nije prijestupna')
    else:
        print(f'Godina {godina} nije prijestupna')