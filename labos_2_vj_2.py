import datetime as dt

'''print(dt.datetime.now())
print(dt.datetime.min)
print(dt.datetime.min - dt.datetime.now())
print((dt.datetime.min - dt.datetime.now()) % dt.timedelta(minutes = 15))
print(((dt.datetime.min - dt.datetime.now()) % dt.timedelta(minutes = 15)) + dt.datetime.now())'''

def zaokruzenoVrijeme():
    trenutno = dt.datetime.now()
    razlika = (dt.datetime.min - dt.datetime.now()) % dt.timedelta(minutes = 15)
    return trenutno + razlika

print(zaokruzenoVrijeme())
