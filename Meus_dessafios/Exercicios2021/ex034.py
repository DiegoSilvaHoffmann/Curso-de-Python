salario = float(input('Informe seu salario atual: R$ '))
print('Seu salario atual é de R${:.2f}'.format(salario))
if salario >= 1250.00:
    print('Voce vai ter uma aumento 10%, ficando seu novo salario em R${:.2f}.'.format(salario * 110 / 100))
else:
    print('Seu salario teve um aumento de 15%, ficando em R${:.2f}.'.format(salario * 115 / 100))
print('Parabens pelo seu aumento!')
