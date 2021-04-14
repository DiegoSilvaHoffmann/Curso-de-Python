from datetime import date
nasc = int(input('Qual seu ano de nascimento? '))
atual = date.today().year
idade = atual - nasc
print('Voce tem {} anos.'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade > 19 and idade <= 25:
    print('Sua categoria é SENIOR')
elif idade > 25:
    print('Sua categoria é MASTER.')
