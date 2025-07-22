
while True:  
    print('GETALLEN GENERATORS')
    print('')

    print('1. Getallenreeks\n2. Tafels van vermenigvuldiging\n3.Quit')
    print('')
    jouw_keuze = int(input('Jouw keuze: '))

    import os            # clears the user interface
    os.system('CLS') 
    
    if jouw_keuze == 1:
        print('Getallenreeks\n')
        startgetal = int(input('Geef een startgetal: '))
        stopgetal = int(input('Geef een stopgetal: '))

        if startgetal <= stopgetal:

            while True:
                startgetal <= stopgetal
                print(startgetal)
                startgetal += 1
                if(startgetal == stopgetal):
                    print(stopgetal)
                    break
        elif(startgetal >= stopgetal):
            while True:
                startgetal > stopgetal
                print(startgetal)   
                startgetal -= 1
                if(startgetal == stopgetal):
                    print(stopgetal)
                    break
    elif(jouw_keuze == 2):
        import os            # clears the user interface
        os.system('CLS')
        print('TAFELS\n')

        getal = 0
        tafelnummer = int(input('Geef tafelnummer: '))

        while getal <= 9:
            getal += 1
            x = getal * tafelnummer
            print(f'{getal} x 'f'{tafelnummer} = 'f'{x}')
    elif(jouw_keuze == 3):
        print('BYE')
        break