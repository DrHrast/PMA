import datetime as dt

def unosGrada():
    gradovi = ['Los Angeles', 'New York', 'London', 'Pariz', 'Moskva', 'Beijing', 'Tokio']
    print(gradovi)
    izbor = input('Unesite jedan od ponuđenih gradova: ')
    while True:
        if not izbor in gradovi:
            izbor = input('Unesite jedan od ponuđenih gradova: ')
            continue
        else:
            break
    return provjeraVremenskeZone(izbor)

def provjeraVremenskeZone(izbor):
    vrijeme_sada = dt.datetime.now()
    sada = vrijeme_sada.strftime('%H:%M:%S')
    if izbor == 'Pariz':
        zona1 = dt.datetime.now()
        print('Vrijeme u Zagrebu: {0}\nVrijeme u {1}: {0}'.format(zona1.strftime('%H:%M:%S'), izbor + 'u'))
    elif izbor == 'Los Angeles':
        zona2 = dt.datetime.now() - dt.timedelta(hours = -9)
        print('Vrijeme u Zagrebu: {2}\nVrijeme u {1}: {0}'.format(zona2.strftime('%H:%M:%S'), izbor + 'u', sada))
    elif izbor == 'New York':
        zona3 = dt.datetime.now() - dt.timedelta(hours = -6)
        print('Vrijeme u Zagrebu: {2}\nVrijeme u {1}: {0}'.format(zona3.strftime('%H:%M:%S'), izbor + 'u', sada))
    elif izbor == 'London':
        zona4 = dt.datetime.now() - dt.timedelta(hours = -1)
        print('Vrijeme u Zagrebu: {2}\nVrijeme u {1}: {0}'.format(zona4.strftime('%H:%M:%S'), izbor + 'u', sada))
    elif izbor == 'Moskva':
        izbor = list(izbor)
        del izbor[-1]
        izbor.append('i')
        str1 = ''
        for i in izbor:
            str1 += i
        zona5 = dt.datetime.now() - dt.timedelta(hours = 2)
        print('Vrijeme u Zagrebu: {2}\nVrijeme u {1}: {0}'.format(zona5.strftime('%H:%M:%S'), str1, sada))
    elif izbor == 'Beijing':
        zona6 = dt.datetime.now() - dt.timedelta(hours = 7)
        print('Vrijeme u Zagrebu: {2}\nVrijeme u {1}: {0}'.format(zona6.strftime('%H:%M:%S'), izbor + 'u', sada))
    elif izbor == 'Tokio':
        zona7 = dt.datetime.now() - dt.timedelta(hours = 8)
        print('Vrijeme u Zagrebu: {2}\nVrijeme u {1}: {0}'.format(zona7.strftime('%H:%M:%S'), izbor + 'u', sada))

unosGrada()