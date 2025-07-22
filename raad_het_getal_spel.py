import random
te_raden = random.randint(1,100)
#print('te raden: 'f'{te_raden}')

aantal_gokken = 0
limiter_up = 100
limiter_down = 1

while True:
    gokje = int(input('Waag een gokje tussen ' f'{limiter_down} en 'f'{limiter_up}: '))
    if gokje >= limiter_down and gokje <= limiter_up:
        if te_raden == gokje:
            aantal_gokken += 1
            print('Joepie! Geraden in 'f'{aantal_gokken} pogingen.')
            if aantal_gokken == 10:
                print(f'Je mag niet meer raden. Het getal was: {te_raden}')
            break
        elif gokje > te_raden:
            print('Het te raden getal is lager.')
            aantal_gokken += 1
            limiter_up = gokje
            
            if aantal_gokken == 10:
                print(f'Je mag niet meer raden. Het getal was: {te_raden}')
                break
            else:
                print('Je mag nog 'f'{10-aantal_gokken} keer raden.')
        elif gokje < te_raden:
            print('Het te raden getal is hoger.')
            aantal_gokken += 1
            limiter_down = gokje
            if aantal_gokken == 10:
                print(f'Je mag niet meer raden. Het getal was: {te_raden}')
                break
            else:
                print('Je mag nog 'f'{10-aantal_gokken} keer raden.')
           
    else:
        aantal_gokken += 0
        print('Ongeldig getal. Je mag nog 'f'{10-aantal_gokken} keer raden.')

