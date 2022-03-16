class Osobna(object):
    def __init__(self, txt1, txt2, txt3):
        self.txt1 = txt1
        self.txt2 = txt2
        self.txt3 = txt3

    def PrviRed(self):
        dok = self.txt1[:2]
        drzava_izdavanja = self.txt1[2:5]
        broj_iskaznice = self.txt1[5:14]
        cheksum1 = self.txt1[14]
        oib = self.txt1[15:26]
        #print(dok, drzava_izdavanja, broj_iskaznice, cheksum, oib, sep = '\n')
        return oib

    def DrugiRed(self):
        datum_rod = self.txt2[:6]
        #datum_rod = datetime.strptime(datum_rod, '%y%m%d')
        datum_rod = datum_rod[4:] + '/' + datum_rod[2:4] + '/' + datum_rod[:2]
        cheksum21 = self.txt2[6]
        spol = self.txt2[7]
        if spol == 'M':
            spol = 'Male/Muško'
        elif spol == 'F':
            spol = 'Female/Žensko'
        datum_isteka = self.txt2[8:14]
        datum_isteka = datum_isteka[4:] + '/' + datum_isteka[2:4] + '/' + datum_isteka[:2]
        cheksum22 = self.txt2[14]
        drzavljanstvo = self.txt2[15:18]
        cheksum23 = self.txt2[-1]
        #print(cheksum23)
        return datum_rod, datum_isteka, drzavljanstvo, spol

    def TreciRed(self):
        imeiprez = ''
        for i in self.txt3:
            if ord(i) != 60:
                imeiprez = imeiprez + i
        index = self.txt3.find('<')
        ime = imeiprez[:5]
        prez = imeiprez[5:]
        #print(ime.capitalize(), prez.capitalize())
        return ime, prez


def IspisPodataka(scan):
    trecina = len(scan) // 3
    prvi_red = scan[:trecina]
    drugi_red = scan[trecina:trecina * 2]
    treci_red = scan[trecina * 2:]

    print('', prvi_red, drugi_red, treci_red, sep = '\n')

    osobna1 = Osobna(prvi_red, drugi_red, treci_red)

    ime, prezime = osobna1.TreciRed()
    datum_rodenja, datum_isteka, drzavljanstvo, spol = osobna1.DrugiRed()
    oib = osobna1.PrviRed()

    print()
    print(ime, prezime)
    print(datum_rodenja, datum_isteka, drzavljanstvo, spol, sep = '\n')
    print(oib)


scan = '''IOHRV123456789701234567890<<<<9709218M2006017HRV<<<<<<<<<<<7PETAR<<HULJEK<<<<<<<<<<<<<<<<<'''

IspisPodataka(scan)