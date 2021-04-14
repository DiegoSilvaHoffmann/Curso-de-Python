a = float(input('Qual a altura da parede?'))
l = float(input('Qual a largura da parede?'))
ar = a * l
t = ar / 2
print('Se a altura é de {:.2f}m, e a largura de {:.2f}m, a area para pintar é de {:.2f}m2.\nCada litro de tinta pinta 2m2, voce vai precisar de {:.1f} litros de tinta.'.format(a, l, ar, t))
