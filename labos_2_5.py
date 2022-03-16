def izracun():
    sekunde = int(input('Unesite vrijeme u sekundama: '))
    sati, ost = divmod(sekunde, 3600)
    minute, sekundi = divmod(ost, 60)

    str_h = 'sati'
    str_m = 'minute'
    str_s = 'sekundi'

    if sati == 1:
        str_h = 'sat'
    if minute % 10 == 0 or minute == 1:
        str_m = 'minuta'
    if sekundi == 1:
        str_s = 'sekunda'

    if sati != 0 and minute != 0 and sekundi != 0:
        print(f'{sati} {str_h}, {minute} {str_m} i {sekundi} {str_s}.')
    elif sati != 0 and minute != 0 and sekundi == 0:
        print(f'{sati} {str_h} i {minute} {str_m}.')
    elif sati != 0 and minute == 0 and sekundi != 0:
        print(f'{sati} {str_h} i {sekundi} {str_s}.')
    elif sati != 0 and minute == 0 and sekundi == 0:
        print(f'{sati} {str_h}.')
    elif sati == 0 and minute != 0 and sekundi != 0:
        print(f'{minute} {str_m} i {sekundi} {str_s}.')
    elif sati == 0 and minute != 0 and sekundi == 0:
        print(f'{minute} {str_m}.')
    elif sati == 0 and minute == 0 and sekundi != 0:
        print(f'{sekundi} {str_s}.')



for i in range(5):
    izracun()