def aumentar(n=0, taxa=0, formato=False):
    a = n + (n * taxa / 100)
    return a if formato is False else moeda(a)


def diminuir(n=0, taxa=0, formato=False):
    d = n - (n * taxa / 100)
    return d if formato is False else moeda(d)


def dobro(n=0, formato=False):
    dos = n + n
    return dos if formato is False else moeda(dos)


def metade(n=0, formato=False):
    met = n / 2
    return met if formato is False else moeda(met)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, au=10, di=5):
    print('-' * 30)
    print('RESUMO DE PRECO'.center(30))
    print('-' * 30)
    print(f'Preco analizado:\t{moeda(n)}')
    print(f'Metade do preco:\t{metade(n, True)}')
    print(f'O dobro do preco:\t{dobro(n, True)}')
    print(f'{au}% de aumento: \t{aumentar(n, au, True)}')
    print(f'{di}% desconto:  \t\t{diminuir(n, di, True)}')
    print('-' * 30)
