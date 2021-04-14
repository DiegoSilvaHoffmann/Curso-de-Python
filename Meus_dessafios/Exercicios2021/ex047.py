print('Imprimir somente numeros pares entre 1 e 50:')
for p in range(1, 51):
    par = p % 2
    if par == 0:
        print(p, end=' ')

print('Fim')