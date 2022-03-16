def pretvorba(temp):
    fah = (temp * 1.8) + 32
    return fah

while True:
    temp = int(input('Unesite temperaturu u °C: '))
    fah = pretvorba(temp)
    if fah < 0:
        break
    else:   
        print(f'Temperatura {temp}°C je {fah}°F u Farenheitima')