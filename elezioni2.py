print("ELEZIONI D'AMERICA")
input()
x = str(input("Inserisci il nome del primo elettore "))
y = str(input("Inserisci il nome del secondo elettore "))
vx = float(input("Quanti voti ha ricevuto alle elezioni " + x + "? "))
vy = float(input("Quanti voti ha ricevuto alle elezioni " + y + "? "))
nomi = []
voti = []
nomi.append(x)
nomi.append(y)
voti.append(vx)
voti.append(vy)
nomi.sort()
print("Ordine alfabetico dei candidati: ", nomi)
voti.sort(reverse= True, key=int)
print("I voti candidati in ordine decrescente", voti)