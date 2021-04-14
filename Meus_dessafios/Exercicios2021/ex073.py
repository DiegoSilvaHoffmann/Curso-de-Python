tabela = ('Internacional', 'Flamengo', 'Atletico-MG', 'Sao Paulo', 'Palmeiras', 'Fluminense',
          'Gremio', 'Atletico-PR', 'Ceara SC', 'Corinthians', 'Santos', 'Atletico-Go',
          'Bragantino', 'Vasco da GAma', 'Bahia', 'Sport Recife', 'Fortaleza',
          'Goias', 'Coritiba', 'Botafogo')
time = str(input('Qual o time voce quer saber? '))
print(f'O {time} esta na posicao {tabela.index(time)+1}.')
print('=' * 40)
print(tabela)
print('-' * 42)
print(f'Os 5 mais bem colocados no campeonato sao: 1-{tabela[0]}, 2-{tabela[1]}, 3-{tabela[2]}, 4-{tabela[3]}, 5-{tabela[4]}.')
print('_' * 45)
print(f'Os ultimos quatro sao: 17-{tabela[-4]}, 18-{tabela[-3]}, 19-{tabela[-2]}, e 20-{tabela[-1]}')
print(sorted(tabela))
print('=' * 40)

