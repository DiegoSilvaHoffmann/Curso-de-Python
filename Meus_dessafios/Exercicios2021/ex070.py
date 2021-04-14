total = maismil = 0
while True:
    nome = str(input('Produto: ')).upper().strip()
    preco = float(input('Preco: '))
    total += preco
    maisba = ''
    if preco >= 1000:
        maismil += 1
    if total == 1:
        maisba = preco
        if preco < maisba:
            maisba = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar comprando? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da sua compra é R${total}.')
print(f'Na sua compra ha produtos de mais de R$1.000,00: {maismil} produto(s).')
print(f'O produto mais barato da compra é {nome}.')
