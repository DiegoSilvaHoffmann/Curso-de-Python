valores = list()
while True:
    num = int(input('Informe um valor: '))
    valores.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
if 5 in valores:
    print('Foi digitado o valor 5.')
else:
    print('Nao costa o valor 5 nessa lista')
valores.sort(reverse=True)
print(f'Foram digitados {len(valores)} numeros.')
print(f'A lista em ordem decrescente ficou {valores}.')
