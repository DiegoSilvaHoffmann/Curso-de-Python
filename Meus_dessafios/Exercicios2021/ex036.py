casa = float(input('Indique o valor do imovel: R$'))
renda = float(input('Qual a renda: R$'))
prazo = int(input('Quantos anos deseja pagar? '))
print('Com o imovel no valor de R${:.2f}.'.format(casa))
print('Com prazo de pagamento de {} anos, e renda de {:.2f}.'.format(prazo, renda))
pagmes = casa / (prazo * 12)

if pagmes <= renda * 30 / 100:
    print('Seu emprestimo foi aprovado!')
    print('A cota mensal de pagamento é de R${:.2f}.'.format(pagmes))
else:
    print('Seu emprestimo nao foi aprovado. Lamentamos.')
