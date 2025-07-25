planten = [
    ('roos', 2.0, 'bloem'),
    ('anjer', 1.5, 'bloem'),
    ('tulp', 2.5, 'bloem'),
    ('schijnaugurk', 7.5, 'klimplant'),
    ('clematis', 8.5, 'klimplant'),
    ('harige tepelcactus', 6.5, 'cactus'),
    ('san pedro', 12, 'cactus')
]
while True:
    max_prijs = input('Geef maximum prijs: ')
    if max_prijs == "":
        break
    else: 
        max_prijs = int(max_prijs)
        soort = input('Geef de soort: ')
        print('')
        gevonden = False  #controleren of iets gevonden is
        i = 1
        print('RESULTATEN: ')
        print('-----------')
        print('')
        for plnt in planten:
            if (plnt[1] <= max_prijs and plnt[2] == soort):       
                print(f'{i}. {plnt[0]}, {plnt[1]} euro')          
                i = i+1
                gevonden = True # iets gevonden
        print('')
        if not gevonden:
            print('Geen resultaat.')
            print('')  
  
