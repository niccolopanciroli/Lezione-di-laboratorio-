stipendio = 0
lavoratore = 0
somma = 0
print("Questo programma ti permette di calcolare la media degli stipendi dei dipendendenti di una azienda")
input()
print("Per terminare di inserire dei dati digitare il numero -1")
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
