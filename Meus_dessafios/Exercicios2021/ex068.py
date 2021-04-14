import random
print('--------- JOGO PAR E IMPAR -----------')
vitoria = 0
while True:
    jogador = int(input('Diga um numero: '))
    comp = random.randint(0, 10)
    soma = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Quer PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {comp}. O total é {soma}')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Voce venceu!')
            vitoria += 1
        else:
            print('VOCE PERDEU!')
            break
    if tipo == "I":
        if soma % 2 == 1:
            print('Voce Venceu!')
            vitoria += 1
        else:
            print('VOCE PERDEU!')
            break
print(f'Voce venceu {vitoria} vezes.')
