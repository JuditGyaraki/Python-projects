todos = []
keuze = ''

while keuze != 'q':
    i = 0
    while(i < len(todos)):
        print(f'{i+1}. {todos[i]}')
        i += 1
    print('')    
    print('t. Toevoegen\nv. Verwijderen\nq. Stop')
    print('')
    keuze = input('Jouw keuze (t, v of q): ')

    if keuze == 't':
        nieuw = input('Geef het nieuwe item: ')
        todos.append(nieuw)
        import os           
        os.system('CLS')
    if keuze == 'v':
        i = None
        try:
            i = int(input('Geef het nummer van het verwijderende item: ')) - 1
            import os           
            os.system('CLS')
        except ValueError:
            print('Foutieve invoer.')

        if i != None:
            if i >= 0 and i < len(todos):
                todos.pop(i)
            else:
                print('Nummer is niet correct.')
