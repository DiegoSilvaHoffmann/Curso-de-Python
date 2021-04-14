pessoas = list()
dados = dict()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Digite somente M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    while True:
        resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responsa S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'B) A media de idade é {media:.1f} anos')
print('C) As mulheres cadatradas sao: ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) As pessoas acima da media de idade sao: ', end=' ')
for p in pessoas:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v} ', end=' ')
        print()
print()
