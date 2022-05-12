def neki_niz(lista, index = 0):
    
    lista2 = []
    if len(lista) == 1:
        print(lista)
    else:
        for i in range(len(lista)):
            if (i + 1) == (len(lista)):
                break
            lista2.append(lista[i] + lista[i + 1])
        neki_niz(lista2)
        print(lista)


lista = [10,9,8,7,6,5,4,3,2,1]

neki_niz(lista)