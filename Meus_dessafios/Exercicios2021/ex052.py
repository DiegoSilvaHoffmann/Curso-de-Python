num = int(input('Informe um numero: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[36m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes.'.format(num, total))
if total == 2:
    print('\033[36mE por isso ele é PRIMO!\033[m')
else:
    print('E por isso ele \033[31mNAO É PRIMO!\033[m')
