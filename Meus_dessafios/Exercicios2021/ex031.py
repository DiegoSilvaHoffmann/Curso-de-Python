distancia = float(input('Qual a distancia da viagem? '))
print('Voce esta prestes a fazer uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    print('Seu percurso vai custar R${:.2f}.'.format(distancia * 0.50))
else:
    print('Sua viagem tem mais de 200km, entao o valor fica R${:.2f}.'.format(distancia * 0.45))
