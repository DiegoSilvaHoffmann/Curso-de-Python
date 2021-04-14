from random import randint
n = (randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15))
print(f'Os 5 numeros sorteados sao: {n[0]}, {n[1]}, {n[2]}, {n[3]}, e {n[4]}.')
print(f'O numero maior é {max(n)}')
print(f'E o numero menor é {min(n)}.')

