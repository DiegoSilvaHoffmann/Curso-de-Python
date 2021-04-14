from random import randint
from time import sleep


def sorteio(lista):
    for cont in range(0, 5):
        n = randint(1, 22)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.4)


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nA soma entre numeros pares é de {soma}.')


numeros = list()
sorteio(numeros)
somapar(numeros)
