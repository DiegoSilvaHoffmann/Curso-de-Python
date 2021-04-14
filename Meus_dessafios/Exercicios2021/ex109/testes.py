from ex109 import moeda
valor = float(input('Informe um valor: R$'))
print(f'A metade de {moeda.moeda(valor)}, é {moeda.metade(valor, True)}.')
print(f'O dobro de {moeda.moeda(valor)}, é {moeda.dobro(valor, True)}.')
print(f'Com aumento de 10%, fica {moeda.aumentar(valor, 10, True)}.')
print(f'Com 15% de desconto, fica {moeda.diminuir(valor, 15, True)}')
