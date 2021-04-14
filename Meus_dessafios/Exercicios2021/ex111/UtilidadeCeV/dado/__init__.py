def leiadinheiro(mens):
    ok = False
    while not ok:
        entrada = str(input(mens)).replace(',', '.').strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERO!! "{entrada}" nao é um valor!\033[m')
        else:
            ok = True
            return float(entrada)
