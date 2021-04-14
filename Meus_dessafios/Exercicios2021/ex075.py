num = (int(input('Digite um numero: ')), int(input('Digite outro: ')),
        int(input('Digite mais um: ')), int(input('Digite o ultimo: ')))
if 9 in num:
    print(f'O numero 9 aparece {num.count(9)}')
else:
    print('O numero 9 nao aparece!')
if 3 in num:
    print(f'O numero 3 aparece na posicao {num.index(3)+1}')
else:
    print('O numero 3 nao aparece.')
for n in num:
    if n % 2 == 0 and n > 0:
        print(f'pares: {n}')
