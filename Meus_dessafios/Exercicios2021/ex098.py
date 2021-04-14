from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= 1
    if p == 0:
        p = 1
    print('-' * 26)
    print(f'A contagem comeca com {i}, até {f}, pulando de {p} em {p}.')
    sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 26)
ini = int(input('INICIO: '))
fim = int(input('FIM:    '))
pas = int(input('PASSO:  '))
sleep(0.5)
contador(ini, fim, pas)
