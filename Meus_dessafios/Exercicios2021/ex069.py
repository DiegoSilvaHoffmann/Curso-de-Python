cont = 0
maior18 = mulher20 = 0
while True:
    print('-' * 24)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        cont += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    if idade > 18:
        maior18 = maior18 + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar o cadastro? ')).upper().strip()[0]
    print('-' * 24)
    if resp == 'N':
        break
print(f'No cadastro tem {maior18} maiores de 18 anos.')
print(f'Foram cadastrados {cont} homens.')
print(f'Das mulheres cadastradas, {mulher20} sao menores de 20 anos.')
print('Fim do cadastro')
