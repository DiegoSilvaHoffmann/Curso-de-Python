print('Lista de Compras')
print('-=' * 20)
prodpre = ('Feijao', 2.50, 'Arroz', 2.00, 'Farinha', 0.75, 'Ovos(24un)', 2.50)
for pos in range(0, len(prodpre)):
    if pos % 2 == 0:
        print(f'{prodpre[pos]:.<30}', end=' ')
    else:
        print(f'R${prodpre[pos]:>7.2f}')
print('=' * 40)