def aumentar(n=0, taxa=0):
    a = n + (n * taxa / 100)
    return a


def diminuir(n=0, taxa=0):
    d = n - (n * taxa / 100)
    return d


def dobro(n=0):
    dos = n + n
    return dos


def metade(n=0):
    met = n / 2
    return met


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
