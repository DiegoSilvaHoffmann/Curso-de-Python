n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('REPROVADO! Sua media foi de {:.1f}.'.format(media))
elif media >= 5.0 and media < 7:
    print('RECUPERACAO! Faltou pouco, sua média foi de {:.1f}.'.format(media))
elif media >= 7.0:
    print('APROVADO! Parabens sua media foi de {:.1f}.'.format(media))
