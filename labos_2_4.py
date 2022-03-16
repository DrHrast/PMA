from random import randint
from datetime import datetime
from datetime import timedelta

vrijeme = '00 00 00'
#globalVar = datetime.strptime(vrijeme, '%H %M %S')
globalVar = 'noć'

def getDioDana():
    global globalVar
    sat = randint(0, 12)
    minute = randint(0, 59)
    sis_vrijeme = datetime.now()
    doba_dana = datetime.now() + timedelta(hours=sat, minutes=minute)
    print(globalVar, sis_vrijeme.strftime('%H:%M:%S'), doba_dana.strftime('%H:%M:%S'), sep= '\n')
    if doba_dana.hour >= 6 and doba_dana.hour < 10:
        doba_dana_str = 'jutro'
    elif doba_dana.hour >= 10 and doba_dana.hour < 12:
        doba_dana_str = 'prijepodne'
    elif doba_dana.hour >= 12 and doba_dana.hour < 17:
        doba_dana_str = 'poslijepodne'
    elif doba_dana.hour >= 17 and doba_dana.hour < 22:
        doba_dana_str = 'večer'
    else:
        doba_dana_str = 'noć'
    if doba_dana_str != globalVar:
        globalVar = doba_dana_str
    print(globalVar, '*' * len('%H:%M:%S'),'', sep= '\n')

for i in range(5):
    getDioDana()