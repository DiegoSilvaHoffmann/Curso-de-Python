matriz = [[], [], []]
for n in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para [0, {n}]: ')))
for c in range(0, 3):
    matriz[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for t in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para [2, {t}]: ')))
print(matriz[0])
print(matriz[1])
print(matriz[2])
