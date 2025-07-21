print('WELKE DIERENVOEDING?\n********************')

#vraag invoer van gebruiker (diersoort)
diersoort = input('Geef een diersoort in (hond of kat): ')
#als verkeerde invoer, print foutmelding en stopt het programma
if(not(diersoort == 'hond' or diersoort == 'kat')):
    print('Diersoort niet herkend.')
else:
    #met while blijft het programma vragen voor leftijd als het kleiner is dan 0
    while True:
        #vraagt leeftijd aan de gebruiker
        leeftijd = int(input('Geef de leeftijd in: '))
        if(leeftijd < 0):
            print('Geef een geldige leeftijd in...')
            import os            # clears the user interface
            os.system('CLS')
            print('WELKE DIERENVOEDING?\n********************')
        elif(diersoort == 'hond' and leeftijd <= 1):
            print('Puppyvoeding')
            break
        elif(diersoort == 'hond' and leeftijd >= 2 and leeftijd <= 7):
            print('Adult hondenvoeding')
            break
        elif(diersoort == 'hond' and leeftijd >= 8):
            print('Senior hondenvoeding')
            break
        elif(diersoort == 'kat' and leeftijd <= 1):
            print('Kittenvoeding')
            break
        elif(diersoort == 'kat' and leeftijd >= 2 and leeftijd <= 7):
            print('Adult kattenvoeding')
            break
        elif(diersoort == 'kat' and leeftijd >= 7):
            print('Senior kattenvoeding')
            break
    

   