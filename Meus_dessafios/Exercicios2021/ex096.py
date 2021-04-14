def area(n1, n2):
    a = n1 * n2
    print(f'A area de um terreno {n1}X{n2} é de {a:.2f}m2.')


l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l, c)
