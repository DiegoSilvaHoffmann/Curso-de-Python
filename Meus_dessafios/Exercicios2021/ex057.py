sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o seu sexo? [M/F] ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('O valor esta incorreto, tente novamente.')
print('Sexo {} anotado.'.format(sexo))
