def main():
    A = trazeni_broj()
    L1, L2 = pogodci(A)
    print(L1, L2, sep = '\n')
    print(predvidanje(L1, L2))

def trazeni_broj():
    while True:
        x = int(input('Unesite proj od 1 do 50: '))
        if x >= 1 and x <= 50:
            return x
        print('Unos ne zadovoljava kriterij.')

def pogodci(A):
    igraca = 'BCDE'
    L1 = []
    for i in igraca:
        pok = int(input(f'{i} korisnik upisuje broj: '))
        L1.append(pok)
    L1.sort()
    L2 = []
    for i in L1:
        razlika = A - i
        L2.append(razlika)
    return L1, L2

def predvidanje(L1, L2):
    rje = []
    for i in range(len(L1)):
        sum = L1[i] + L2[i]
        rje.append(sum)
    print(f'Broj koji je korinik A unio je {rje[0]}')
        

main()