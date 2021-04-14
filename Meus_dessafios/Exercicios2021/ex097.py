def escreva(txt):
    tam = len(txt)
    print('-' * tam)
    print(txt)
    print('-' * tam)


algo = str(input('O que quer escrever? ')).strip()
escreva(algo)
