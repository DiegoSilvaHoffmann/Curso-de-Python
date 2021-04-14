n = soma = total = 0
print('Digite qualquer valor. Qaundo quiser parar, digite 999')
while n != 999:
    n = int(input('Digite um numero: '))
    soma = soma + n
    total = total + 1
    if n == 999:
        print('A soma entre os {} numeros digitados é {}.'.format((total - 1), (soma - 999)))
print('fim')
