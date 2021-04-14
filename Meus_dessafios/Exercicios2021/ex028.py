import random
from time import sleep
sorteio = random.randint(0, 5)
jogador = int(input('Tente adivinhar o numero que estou pensando, de 0 a 5: '))
print('PROCESSANDO...')
sleep(2)
if sorteio == jogador:
    print('Parabens! Eu pensei no numero {}!'.format(sorteio))
else:
    print('Voce errou, tente novamente!')
