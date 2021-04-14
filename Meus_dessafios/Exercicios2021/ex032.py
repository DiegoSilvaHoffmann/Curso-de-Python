ano = int(input('Que ano quer analizar?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Biseexto.'.format(ano))
else:
    print('Esse ano nao é Bissexto!')
