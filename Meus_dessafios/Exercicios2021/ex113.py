def leiaint(msg):
   while True:
       try:
           n = int(input(msg))
       except (ValueError, TypeError):
           print('\033[31mERRO! Digite um valor valido!\033[m')
           continue
       except (KeyboardInterrupt):
           print('\033[35mUsuario nao deseja continuar\033[m')
           return 0
       else:
           return n


def leiaFloat(mens):
    while True:
        try:
            n = float(input(mens))
        except (ValueError, TypeError):
            print('\033[31mERRO!!! Digite uma REAL!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[35mO usuario nao deseja seguir...\033[m')
            return 0
        else:
            return n


n1 = leiaint('Digite um Inteiro: ')
n2 = leiaFloat('Digite um valor Real: ')
print(f'O valor inteiro digitado foi {n1}, e um Real {n2}')
