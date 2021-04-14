def fatorial(num, show=False):
    """
    -> Calculo de fatorial
    :param num: O numero qu deseja saber o fatorial
    :param show: Se quer ver o calculo
    :return: O resultado, o fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end=' ')
            if c > 1:
                print('X', end=' ')
            else:
                print(' = ', end=' ')
    return f


n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é {fatorial(n)}.')
print(fatorial(n, show=True))
