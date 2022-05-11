from pickle import NONE


class Dll(object):
    _index = 0

    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.previous = prev
        Dll._index += 1
        self._index = Dll._index

    def lenlist(self):
        return Dll._index
    
    def printing(self):
        if self.next == None:
            print(self.value)
        else:
            print(self.value)
            Dll.printing(self.next)

    def provjeraIndexa(self):
        while self._index != Dll._index:
            self = self.next  
        Dll.reversPrinting(self) 
        
    def reversPrinting(self):
        if self.previous == None:
            print(self.value)
        elif self.next == None:
            print(self.value)
            Dll.reversPrinting(self.previous)
        else:
            print(self.value)
            Dll.reversPrinting(self.previous)

clan1 = Dll('Jedan')
clan2 = Dll('Dva', None, clan1)
clan1.next = clan2
clan0 = Dll('Nula', clan1)
clan1.previous = clan0
clan3 = Dll('Tri', None, clan2)
clan2.next = clan3
#print(clan1.previous.value, clan1.next.value)

nclan1 = Dll('Ponedjeljak')
nclan2 = Dll('Utorak', None, nclan1)
nclan1.next = nclan2
nclan3 = Dll('Srijeda', None, nclan2)
nclan2.next = nclan3

clan3.next = nclan1
nclan1.previous = clan3

#clan0.printing()
#clan0.reversPrinting()
#nclan2.reversPrinting()
nclan3.provjeraIndexa()