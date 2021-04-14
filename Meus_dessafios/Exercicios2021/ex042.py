print('Vamos verificar se estas medidas formam um triangulo')
r1 = float(input('Informe a primeira medida: '))
r2 = float(input('Informe a segunda medida: '))
r3 = float(input('Informa a terceira medida: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r2:
    print('Formam triangulo.')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('nao formam triangulo')
