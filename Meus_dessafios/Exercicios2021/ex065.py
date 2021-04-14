resp = 'S'
soma = media = cont = maior = menor = 0
while resp == 'S':
    n = int(input('Digite um valor: '))
    resp = str(input('QUER CONTINUAR? ')).strip().upper()[0]
    cont = cont + 1
    soma = soma + n
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print('Voce digitou {} numeros, e a media é {}.'.format(cont, media))
print('O numero maior digitado foi {} e o menor {}.'.format(maior, menor))
print('Fim')
