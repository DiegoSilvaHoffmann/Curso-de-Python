num = int(input('Digite um numero: '))
par = (num % 2)
if par == 0:
    print('Este numero {}, é par!'.format(num))
else:
    print('Este numero {}, é impar.'.format(num))
