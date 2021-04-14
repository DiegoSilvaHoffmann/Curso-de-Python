from time import sleep


def maior(*num):
    cont = maior = 0
    print('Analisando os numeros...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    sleep(0.5)
    print(f'O maior é {maior}', flush=True)


maior(12, 45, 3, 8, 17, 9, 66, 13)
maior(4, 6, 90, 3, 11, 12)
maior(5, 12, 7, 3, 8)
maior(16)
