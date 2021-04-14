termo = int(input('Informe o termo: '))
razao = int(input('Qual a razao: '))
limite = termo + (10 - 1) * razao
for n in range(termo, limite + razao, razao):
    print(n, end=' ->')
print('Fim')
