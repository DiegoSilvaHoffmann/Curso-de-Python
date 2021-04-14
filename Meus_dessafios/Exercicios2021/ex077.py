palavras = ('CURSO', 'TRABALHO', 'ESTUDAR', 'SONHO', 'TRANQUILIDADE')
for p in palavras:
    print(f'\nA palavra {p} tem as vogais: ', end=' ')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end='')
