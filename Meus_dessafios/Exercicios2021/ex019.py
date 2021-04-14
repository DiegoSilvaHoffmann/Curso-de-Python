import random
a1 = input('Qual o nome do primeiro aluno: ')
a2 = input('Qual o nome do segundo aluno: ')
a3 = input('Qual o nome do terceiro aluno: ')
a4 = input('Qual o nome do quarto aluno: ')
sorteio = [a1, a2, a3, a4]
escolha = random.choice(sorteio)
print('O escolhido para apagar o quadro foi: {}.'.format(escolha))
