peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura?(m) '))
imc = peso / (altura * altura)
print('Seu IMC é de {:.2f}.'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso normal.')
elif 18.5 <= imc < 25:
    print('Seu peso esta ideal!')
elif 25 < imc <= 30:
    print('Voce esta com sobrepeso, se exercite.')
elif imc > 30 and imc <= 40:
    print('Voce esta com obesidade.')
else:
    print('Voce tem Obesidade morbida, procure ajuda medica.')
