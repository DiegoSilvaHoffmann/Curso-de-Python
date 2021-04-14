dis = float(input('Qual a distancia percorrida com o carro? '))
dias = int(input('Quantos dias o carro foi alugado?'))
km = dis * 0.15
diaria = dias * 60
print('Voce percorreu {:.2f}Km com o carro. Cada km custa R$0,15, seu total a pagar é de R${:.2f}.'.format(dis, km))
print('O carro foi alugado por {:.0f} dias. A diaria é de R$60,00, seu custo pelos dias é de R${:.2f}.'.format(dias, diaria))
print('O total a pagar pelo aluguel de {:.0f} dias e {:.2f} rodados, é de R${:.2f}.'.format(dias, dis, km + diaria))
