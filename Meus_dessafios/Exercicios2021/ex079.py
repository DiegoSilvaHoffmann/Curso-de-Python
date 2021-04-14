valores = list()
while True:
    num = int(input('Informe um numero: '))
    if num not in valores:
        valores.append(num)
        print('O numero Foi adicionado!!!')
    else:
        print('Este valor já tem!')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer acrescentar mais numeros? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
valores.sort()
print(f'Os valores digitados foram {valores}.')
