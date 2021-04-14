produto = float(input('Qual o valor da compra? R$'))
forma = input('Como voce quer pagar, dinheiro ou cartao? ').upper()
if forma == 'CARTAO':
    dividido = int(input('Em quantas vezes quer pagar? '))
if forma == 'DINHEIRO':
    print('Entao voce tem 10% de desconto.')
    print('O valor vai ficar em R${:.2f}.'.format(produto * 90 / 100))
elif dividido == 1:
    print('Entao voce tem 5% de desconto.')
    print('O valor da compra fica R${:.2f}.'.format(produto * 95 / 100))
elif dividido == 2:
    print('o valor do produto é R${:.2f}.'.format(produto))
    print('Parcelado ficara duas vezes de R${:.2f}, sem juros.'.format(produto / 2))
elif dividido >= 3:
    print('Parcela a partir de 3x, tem juros de 20%.')
    print('O valor de cada parcela é R${:.2f}.'.format((produto * 120 / 100) / dividido))
