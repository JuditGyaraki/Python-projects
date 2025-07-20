dag = 1
neerslag_totaal = 0
neerslag_dag = 0

print("Frank's hulp-programma")
print('----------------------')

while neerslag_dag >= 0:
    neerslag_dag = float(input(f'Geef de neerslag voor de dag {dag} in mm:'))
    neerslag_totaal = neerslag_dag + neerslag_totaal
    dag = dag + 1

print(f'De gemiddelde neerslag was {neerslag_totaal/dag} mm de afgelopen {dag-1} dagen.')