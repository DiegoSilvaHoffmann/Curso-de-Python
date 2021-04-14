import math
catO = float(input('Informe o valor do cateto Oposto: '))
catA = float(input('Informe o valor do cateto Adjacente: '))
Hip = math.hypot(catO, catA)
print('A Hipotenusa do cateto Oposto {:.2f}, e do Adjacente {:2f}, é {:.2f}.'.format(catO, catA, Hip))
