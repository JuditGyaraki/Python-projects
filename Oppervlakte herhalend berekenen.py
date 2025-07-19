while True:
    print('OPPERVLAKTE BEREKENEN\n---------------------\n1. Rechhoek\n2. Driehoek\n3. Cirkel\n4. Stop')
    keuze = input('Jouw keuze (1, 2, 3 of 4): ')
    if keuze == '4':
        print('Bye!')
        break
    elif(keuze == '1'):
        breedte = float(input('Geef de breedte: '))
        hoogte =  float(input('Geef de hoogte: '))
        print('De oppervlakte van de rechthoek is ' f'{breedte*hoogte}cm²')
        text = input("Druk enter om terug te keren naar het menu...")
        if text == "":
            import os            # clears the user interface
            os.system('CLS')
    elif(keuze == '2'):
        basis = float(input('Geef de basis: '))
        halve_hoogte= float(input('Geef de halve van de hoogte: '))
        print('De oppervlakte van de driehoek is ' f'{basis*halve_hoogte}cm²')
        text = input("Druk enter om terug te keren naar het menu...")
        if text == "":        
            import os           
            os.system('CLS')
    elif(keuze == '3'):
        from math import pi     # import from math library
        straal = float(input('Geef de straal van de cirkel: '))
        print('De oppervlakte van de cirkel is ' f'{pi * straal**2}cm²')
        text = input("Druk enter om terug te keren naar het menu...")
        if text == "":
            import os           
            os.system('CLS')
