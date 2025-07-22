switch = True
n = 0
import random
kogel = random.randint(1,6)

while n < 6:
    if switch:
        invoer = input('Speler 1 is aan de beurt...druk enter...')
        if kogel != n:
            print('Klik"...Je hebt geluk...')
        else:
            print('KNAL! Speler 1 is dood...')
            break    


    else:
        invoer = input('Speler 2 is aan de beurt...druk enter...')
        if kogel != n:
            print('Klik"...Je hebt geluk...')
        else:
            print('KNAL! Speler 2 is dood...')
            break
      
    switch = not switch
    n = n + 1