soma = 0
mediaID = 0
maioridadehomi = 0
homi = ''
totalmulher20 = 0
for pess in range(1, 5):
    print('---------{}a PESSOA--------'.format(pess))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(M ou F): ')).upper()
    soma += idade
    if pess == 1 and sexo == 'M':
        maioridadehomi = idade
        homi = nome
    if sexo in 'M' and idade > maioridadehomi:
        maioridadehomi = idade
        homi = nome
    if sexo in 'F' and idade < 20:
        totalmulher20 += 1
mediaID = soma / 4
print('A media de idade é {:2} anos.'.format(mediaID))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomi, homi))
print('Na lista tem {} mulheres menores de 20 anos.'.format(totalmulher20))

