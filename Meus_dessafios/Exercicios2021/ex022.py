nome = str(input('Digite um nome: ')).strip()
separa = nome.split()
print('Seu nome em maiusculas {}'.format(nome.upper()))
print('Seu nome em minusculas {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {}, e tem {} letras.'.format(separa[0], len(separa[0])))

