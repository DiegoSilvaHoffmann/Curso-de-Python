frase = str(input('Escreve uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
invertido = junto[::-1]

if invertido == junto:
    print('A frase é PALINDROMO')
else:
    print('A frase nao é PALINDROMO.')
print('A palavra {}, fica assim {}.'.format(frase, invertido))
