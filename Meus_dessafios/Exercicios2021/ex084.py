pessoas = list()
dados = list()
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso(Kg): ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 30)
print(f'O maior peso foi de {mai}Kg, e as pessoas mais pesadas sao: ')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}')
print('-' * 30)
print(f'O menor peso foi de {men}Kg. E as pessoas mais leves: ')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}')
print('-' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas')
