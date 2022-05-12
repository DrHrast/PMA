from random import randint

def bin_sort(lista, index = 0):
    lista2 = []
    a = lista[index]
    if a not in lista2:
        lista2.append(a)
    elif a > lista2[-1]:
        lista2.append(a)
    else:
        bin_sort(lista2, 0)
    

def back_track(brojevi):
    bin_sort(brojevi)
    for i in brojevi:
        for j in brojevi:
            for k in brojevi:
                if i == j or j == k or j < i or k < j:
                    continue
                elif i + j + k == 22:
                    print(f'{i} + {j} + {k} = {i + j + k}')

brojevi = [randint(1, 30) for i in range(10)]

back_track(brojevi)
print(brojevi)