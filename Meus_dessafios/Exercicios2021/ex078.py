num = list()
maior = menor = 0
for c in range(0, 5):
    num.append(int(input(f'Digite um valor na posicao {c}: ')))
    if c == 0:
        maior = num[c]
        menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if menor > num[c]:
            menor = num[c]
for pos, v in enumerate(num):
    if v == maior:
        print(f'O maior numero {maior} esta na posicao {pos}...')
    if v == menor:
        print(f'O menor valor é {menor}, e sua posicao é {pos}...')
print(num)
