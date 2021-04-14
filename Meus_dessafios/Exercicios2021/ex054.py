from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {} nasceu a pessoa: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('Temos {} pessoas maiores de idade.'.format(totmaior))
print('E temos {} menores de idade.'.format(totmenor))


