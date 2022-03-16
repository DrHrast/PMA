while True:
    prvi_kol = int(input('Rezultat prvog kolokvija: '))
    drugi_kol = int(input('Rezultat drugog kolokvija: '))
    treci_kol = int(input('Rezultat trećeg kolokvija: '))
    if prvi_kol < 50 or drugi_kol < 50 or treci_kol < 50:
        print('Student nije prošao')
    else:
        ukupni_pos = (prvi_kol + drugi_kol + treci_kol) / 3
        if ukupni_pos > 50 and ukupni_pos <= 65:
            print('Ocijena 2')
        elif ukupni_pos > 65 and ukupni_pos <= 75:
            print('Ocijena 3')
        elif ukupni_pos > 75 and ukupni_pos <= 90:
            print('Ocijena 4')
        else:
            print('Ocijena 5')