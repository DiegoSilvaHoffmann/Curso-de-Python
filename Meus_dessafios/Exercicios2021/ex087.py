matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor da posicao [{l}, {c}]: '))
        soma3 = soma3 + (matriz[l][2])
        if matriz[l][c] % 2 == 0:
            soma = soma + matriz[l][c]
        if c == 0:
            maior = (matriz[1][c])
        else:
            if matriz[1][c] > maior:
                maior = (matriz[1][c])
print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
print('-' * 35)
print(f'A soma dos numeros pares é {soma}.')
print(f'A soma da terceira coluna é {soma3}.')
print(f'O maior valor da segunda linha é {maior}.')
