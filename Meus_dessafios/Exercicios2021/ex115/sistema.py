from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver lista de Cadastro', 'Cadastrar pessoas', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leiaint('Idade: ')
        cadastro(arq, nome, idade)
    elif resposta == 3:
        titulo('Saindo do sistema... Volte sempre!')
        break
    else:
        print('\033[36mERRO! Digite uma opcao valida\033[m')
    sleep(1.6)
