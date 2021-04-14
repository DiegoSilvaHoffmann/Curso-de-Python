jogador = dict()
gol = list()
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    gol.append(int(input(f'  Quantos gols na partida {c}? ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} trem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} teve {partidas}.')
for i, v in enumerate(jogador['gols']):
    print(f'  Na partida {i} fez {v} gols.')
print(f'Com todas de {jogador["total"]} de gols')
