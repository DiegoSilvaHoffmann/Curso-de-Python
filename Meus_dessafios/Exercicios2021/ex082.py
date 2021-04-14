pares = list()
impar = list()
while True:
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        pares.append(num)
        print('Este numero foi adicionado a lista de PARES!')
    else:
        impar.append(num)
        print('Este numero foi adicionado a lista de IMPARES.')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).upper().strip()[0]
    if resp == 'N':
        break
lista = pares + impar
print(f'A lista completa é {lista}.')
print(f'Os numeros PARES sao {pares}.')
print(f'E os numeros impares: {impar}.')
