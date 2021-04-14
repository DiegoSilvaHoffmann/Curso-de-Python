lista = list()
for c in range(0, 5):
    num = int(input('Informe um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Vai ser inserido na ultima posicao...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Vai ser inserido na posicao {pos}')
                break
            pos += 1
print(f'A lista em ordem ficou {lista}.')
