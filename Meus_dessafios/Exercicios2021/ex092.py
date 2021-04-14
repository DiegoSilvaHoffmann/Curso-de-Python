from datetime import date
ficha = dict()
dados = list()
atual = date.today().year
for c in range(1):
    ficha['Nome'] = str(input('Nome: '))
    Ano = int(input('Ano de nascimento: '))
    ficha['idade'] = atual - Ano
    ficha['cart'] = int(input('No. Carteira de Trabalho(0 nao tem): '))
    if ficha['cart'] == 0:
        dados.append(ficha.copy())
        print(dados)
        break
    else:
        ficha['anocont'] = int(input('Ano de Contratacao: '))
        ficha['salario'] = float(input('Salario: R$'))
        ficha['falta'] = 35 - (atual - ficha['anocont'])
        ficha['aposenta'] = ficha['falta'] + ficha['idade']
    dados.append(ficha.copy())
    print(f'O {ficha["Nome"]} tem {ficha["idade"]} anos, trabalha desde {ficha["anocont"]}.')
    print(f'Para se aposentar, faltam {ficha["falta"]} anos. Ele vai se aposentar com {ficha["aposenta"]} anos.')
