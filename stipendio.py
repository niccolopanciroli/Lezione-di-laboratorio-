stipendio = 0
lavoratore = 0
somma = 0
while stipendio != -1:
    stipendio = float(input("Inserisci stipendio lavaratore "))
    somma = stipendio + somma
    lavoratore= lavoratore +1
    media= somma/lavoratore
    if stipendio == -1:
        somma= somma +1  #annullo la presenza del -1
        lavoratore= lavoratore -1 #elimino il lavoratore con stipendio -1
        media= somma/lavoratore
print("Media: ", media)
