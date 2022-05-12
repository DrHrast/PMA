def BinarnoPretrazivanje(lista, cilj, high, low):
    median = 0
    if high >= low:
        median = (low + high) // 2
        if lista[median] == cilj:
            return median
        elif lista[median] > cilj:
            high = median - 1
            return BinarnoPretrazivanje(lista, cilj, high, low)
        else:
            low = median + 1
            return BinarnoPretrazivanje(lista, cilj, high, low)
    else: 
        return -1


lista = [0,1,2,5,8,10,12,16,17,20,21,22,25,32,39,40,41,42]

high = len(lista) - 1
rez = BinarnoPretrazivanje(lista, 5, high, 0)
if rez != -1:
    print(f'Element je na indexu {str(rez)}')
else:
    print('Nema traženog elementa')