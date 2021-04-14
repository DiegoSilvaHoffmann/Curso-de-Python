nome = str(input('Informe seu nome completo: ')).strip()
n = nome.split()
print('Olá, seu primeiro nome é {}'.format(n[0]))
print('E seu ultimo sobrenome é {}, seja bem vindo!'.format(n[len(n) - 1]))
