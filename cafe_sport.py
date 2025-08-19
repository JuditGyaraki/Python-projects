dranken = [
        ['cola', 2], 
        ['capri-sun', 2], 
        ['chocomelk', 1.75], 
        ['thee', 2.5]
        ]

bestellingen = []
som = 0

import os
import time

while True:
        os.system('cls')
        print('BESTELLINGEN\n~~~~~~~~~~~~~')
        for i in range(len(bestellingen)):
                print(f'{i + 1}. {bestellingen[i][0]} - {bestellingen[i][1]} euro')        
        print()   
        print('DRANKENKAART\n~~~~~~~~~~~~\n1. cola - 2 euro\n2. capri-sun - 2 euro\n3. chocomelk 1.75 euro\n4. thee - 2.5 euro')
        print()
        print('1. Bestellen\n2. Afrekenen\n3. Stop')
        print()
        menukeuze = None
        drankenkeuze = None
        try:
                menukeuze = int(input('Je keuze (1, 2 of 3): '))
                if menukeuze < 1 or menukeuze > 3:
                        print('1, 2 of 3')
                        time.sleep(5)

        except ValueError:
                print('1, 2 of 3')
                time.sleep(5)
                
        if menukeuze == 1:
                try:
                        drankenkeuze = int(input('Geef de dranknummer in om toe te voegen aan bestelling: '))
                        drankenkeuze = drankenkeuze - 1
                        bestellingen.append(dranken[drankenkeuze])
                except IndexError:
                        print('1, 2, 3 of 4')
                        time.sleep(10)
        elif menukeuze == 2:

                print('AFREKENEN\n~~~~~~~~')
                for i in range(len(bestellingen)):
                        print(f'{i + 1}. {bestellingen[i][0]} - {bestellingen[i][1]} euro')        
                print()
                for p in bestellingen:
                        som = som + p[1]
                print(f'TOTAAL: {som} euro')
                afrekenen = input('Afrekenen: j/n ')
                if afrekenen == "j":
                        bestellingen = []
                elif afrekenen == 'n':
                        continue
        elif menukeuze == 3:
                break




    
    
    





    
    

