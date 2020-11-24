giorno = 0
somma= 0
veicoli = 1
while veicoli != 0:
    veicoli= int(input("Quanti veicoli sono passati oggi al casello autostradale? "))
    giorno = giorno +1
    somma = somma + veicoli
    if veicoli == 0:
        giorno= giorno-1
print("In ", giorno," giorni, sono passati ", somma, " veicoli")