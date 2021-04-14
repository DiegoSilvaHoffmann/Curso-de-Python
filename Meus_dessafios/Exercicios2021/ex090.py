ficha = dict()
ficha['Aluno'] = str(input('Nome: '))
ficha['Media'] = float(input(f'Média de {ficha["Aluno"]}: '))
print('-=' * 30)
print(f'O nome do aluno é {ficha["Aluno"]}')
print(f'A média do aluno é {ficha["Media"]}')
if ficha['Media'] > 7:
    ficha['situacao'] = 'Aprovado'
elif 5 <= ficha['Media'] < 7:
    ficha['situacao'] = 'Recuparacao'
else:
    ficha['situacao'] = 'Reprovado'
print('-=' * 30)
for k, v in ficha.items():
    print(f' -  {k} é igual a {v}.')
