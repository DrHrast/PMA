uvijet_panagrama = 'abcdefghijklmnopqrstuvwxyz'
provjera_panagrama = ''
recenica = input('Unesite rečenicu:\n')
for i in uvijet_panagrama:
    if i in recenica:
        provjera_panagrama = provjera_panagrama + i

if len(provjera_panagrama) == len(uvijet_panagrama):
    print('Rečenica je panagram')
else:
    print('Rečenica nije panagram')

#primjer panagrama: The quick brown fox jumps over the lazy dog