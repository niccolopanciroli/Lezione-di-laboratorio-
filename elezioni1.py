print("VINCITORE DELLE ELEZIONI")
Biden = int(input("Quanti voti ha ricevuto Biden alle elezioni? "))
Trump = int(input("Quanti voti ha ricevuto Trump alle elezioni? "))
GE = Biden + Trump 
pbiden = (Biden*100)/GE
ptrump = (Trump*100)/GE

if pbiden > ptrump:
    print("Biden ha vinto le elezioni con il", pbiden," dei voti")
elif ptrump > pbiden:
    print("Trump ha vinto le elezioni con il", ptrump," dei voti")    