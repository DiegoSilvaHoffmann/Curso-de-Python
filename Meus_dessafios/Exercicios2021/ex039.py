from datetime import date
ano = int(input('Indique o ano de seu nascimento: '))
sexo = str(input('Indique seu sexo (M ou F): ')).upper()
atual = date.today().year
idade = atual - ano
if sexo == 'F':
    print('O alistamento nao é obrigatorio para mulheres.')
if sexo == 'M' and idade == 18:
    print('Esta na hora de se alistar, voce ja esta no ano de completar {} anos.'.format(idade))
elif sexo == 'M' and idade < 18:
    saldo = 18 - idade
    ano = saldo + atual
    print('Ainda faltam {} anos para voce se alistar.'.format(saldo))
    print('Voce deve se alistar em {}.'.format(ano))
elif sexo == "M" and idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Já passaram {} do seu alistamento.'.format(saldo))
    print('Voce deve ou deveria ter se alistado em {}.'.format(ano))

