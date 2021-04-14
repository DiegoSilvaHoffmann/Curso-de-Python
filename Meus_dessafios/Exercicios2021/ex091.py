from random import randint
from operator import itemgetter
from time import sleep
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}

ranking = list()
for k, v in jogo.items():
    print(f'{k} sorteou {v} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 15)
sleep(1)
print('   == RANKING ==')
sleep(1)
for i, j in enumerate(ranking):
    print(f'{i+1}o. - {j[0]} tirou {j[1]}')
    sleep(1)

