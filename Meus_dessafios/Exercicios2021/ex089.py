lista = list()
alunos = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    alunos.append(nome)
    alunos.append(n1)
    alunos.append(n2)
    lista.append(alunos[:])
    alunos.clear()
    resp = " "
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
for i, p in enumerate(lista):
    media = (p[1] + p[2]) / 2
    print(f'{i}o. {p[0]} com media de: {media}')
while True:
    print('-=' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 interromep) '))
    if opc == 999:
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} sao {lista[opc][1]} e {lista[opc][2]}')
print('Volte sempre!')
