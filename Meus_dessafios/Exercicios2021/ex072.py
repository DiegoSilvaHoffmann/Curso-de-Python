cont = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete',
        'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    escolha = int(input('Digite um numero de 0 a 20: '))
    if 0 <= escolha <= 20:
        break
print(f'O numero que voce digitou foi {cont[escolha]}!')


