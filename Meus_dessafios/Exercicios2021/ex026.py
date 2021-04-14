frase = str(input('Escreva alguma frase: ')).strip().upper()
print('A letra A, aparece {} vezes.'.format(frase.count('A')))
print('A letra A aparece a primeira vez na posicao {}.'.format(frase.find('A') + 1))
print('A ultima vez que aparece a letra A, é na posicao {}'.format(frase.rfind('A') + 1))
