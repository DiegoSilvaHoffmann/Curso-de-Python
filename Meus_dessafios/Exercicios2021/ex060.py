import math
n = int(input('Digite um numero: '))
f = math.factorial(n)
print('O fatorial de {} é {}.'.format(n, f))



n = int(input('Digite um numero para calcular o fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else " = ", end='')
    f = f * c
    c -= 1
print('{}'.format(f))
