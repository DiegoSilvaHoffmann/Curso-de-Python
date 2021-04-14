carro = float(input('Informe a velocidade: '))
multa = (carro - 80) * 7
if carro > 80:
    print('Voce esta acima do limite de 80Km/h!')
    print('Isso vai gerar uma multa de R${:.2f}.'.format(multa))
print('Tenha um bom dia! Dirija com seguranca.')
