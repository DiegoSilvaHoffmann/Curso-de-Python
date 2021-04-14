import math
angulo = float(input('Informe o angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Com angulo de {}'.format(angulo))
print('Seu Seno é de {:.2f}, o Cosseno de {:.2f}, e tangente de {:.2f}'.format(seno, cosseno, tangente))
