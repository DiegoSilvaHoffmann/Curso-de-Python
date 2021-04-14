from ex108 import moeda
valor = float(input('Informe um valor: R$'))
print(f'A metade de {moeda.moeda(valor)}, é {moeda.moeda(moeda.metade(valor))}.')
print(f'O dobro de {moeda.moeda(valor)}, é {moeda.moeda(moeda.dobro(valor))}.')
print(f'Com aumento de 10%, fica {moeda.moeda(moeda.aumentar(valor, 10))}.')
print(f'Com 15% de desconto, fica {moeda.moeda(moeda.diminuir(valor, 15))}')
