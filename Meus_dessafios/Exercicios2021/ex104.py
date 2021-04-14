def leiaint(mens):
    ok = False
    valor = 0
    while True:
        n = str(input(mens))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um numero!\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar {n}.')