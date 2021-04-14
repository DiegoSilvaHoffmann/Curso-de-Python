def ficha(a='', b=0):
    if a == '':
        a = '<DESCONHECIDO>'
    return f'O jogador {a}, fez {b} gol(s).'


nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
print(ficha(nome, gols))
