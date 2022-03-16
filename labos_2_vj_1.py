from datetime import datetime

def ispis_vremena():
    sati = datetime.now()
    datum = datetime.now()
    return datum.strftime('%Y/%m/%d'), sati.strftime('%H:%M:%S')

print(ispis_vremena())