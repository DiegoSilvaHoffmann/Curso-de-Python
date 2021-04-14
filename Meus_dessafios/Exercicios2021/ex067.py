print('-' * 30)
while True:
    n = int(input('Indique o numero da Tabuada: '))
    if n < 0:
        break
    print('-' * 30)
    for t in range(1, 11):
        print(f'{n} X {t:2} = {n * t}')
print('Fim do programa')
