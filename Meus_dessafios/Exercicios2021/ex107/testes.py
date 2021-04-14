from ex107 import moeda
valor = float(input('Informe um valor: R$'))
print(f'A metade de R${valor}, é R${moeda.metade(valor)}.')
print(f'O dobro de R${valor}, é R${moeda.dobro(valor)}.')
print(f'Com aumento de 10%, fica R${moeda.aumentar(valor, 10)}.')
print(f'Com 15% de desconto, fica R${moeda.diminuir(valor, 15)}')
