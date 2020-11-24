print("ELEZIONI D'AMERICA")
Biden = int(input("Quanti voti ha ricevuto Biden alle elezioni? "))
Trump = int(input("Quanti voti ha ricevuto Trump alle elezioni? "))
candidati = []
nomi = ["Trump", "Biden"]
candidati.append(Biden)
candidati.append(Trump)
nomi.sort()
print("Elenco partecipanti in ordine alfabetico", nomi)
if Biden > Trump:
    print("Elenco in base al punteggio in ordine decrescente", candidati)
elif Trump > Biden:
    candidati.reverse()
    print("Elenco in base al punteggio in ordine decrescente", candidati)