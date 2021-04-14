temp = []
unica = []
pares = list()
impares = []
for num in range(1, 8):
    dig = int(input(f'Informe o {num}o numero: '))
    if dig % 2 == 0:
        pares.append(dig)
        pares.sort()
        temp.clear()
    else:
        impares.append(dig)
        impares.sort()
        temp.clear()
unica.append(pares[:])
unica.append(impares[:])
pares.clear()
impares.clear()
print(f'Os numeros pares sao: {unica[0]}.')
print(f'Os numeros impares sao: {unica[1]}')
