maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('Qual o peso da {} pessoa: '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('A pessoa pesa mais tem {}Kg.'.format(maior))
print('A pessoa pesa menos tem {}Kg.'.format(menor))

