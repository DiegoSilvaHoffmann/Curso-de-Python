soma = 0
for n in range(1, 7):
    num = (int(input('Informe o {} valor: '.format(n))))
    if num % 2 == 0:
            soma = soma + num
print('A soma dos numeros pares é {}.'.format(soma))
