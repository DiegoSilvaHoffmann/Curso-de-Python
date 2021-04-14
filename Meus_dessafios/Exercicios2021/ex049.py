n = int(input('Qual numero voce quer saber a tabuada? '))
for t in range(1, 11):
    print('{} X {:2} = {}'.format(n, t, (n * t)))
