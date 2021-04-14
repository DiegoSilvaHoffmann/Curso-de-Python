import random
print('--------------------------------------------')
sorteio = random.randint(0, 10)
total = 0
jogador = ''
while jogador != sorteio:
    jogador = int(input('Tente adivinhar o numero em que estou pensando de 0 e 10: '))
    if jogador == sorteio:
        print('**********************************************************')
        print('MUITO BEM!! Eu realmente estava pensando no numero {}.'.format(sorteio))
    else:
        if jogador < sorteio:
            print('Mais... Tente novamente.')
        elif jogador >sorteio:
            print('Menoss... Tente outra vez.')
    total = total + 1
print('-------------------------------------------------------')
print('Voce tentou {} vezes.. hahaha!'.format(total))
