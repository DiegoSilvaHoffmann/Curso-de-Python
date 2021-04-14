def notas(* num):
    maior = cont = menor = 0
    situacao = ''
    for valor in num:
        if cont == 0:
            maior = valor
            menor = valor
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
        cont += 1
    media = sum(num) / len(num)
    if 6.5 < media < 8:
        situacao = 'Razoavel'
    elif media > 8:
        situacao = 'EXCELENTE!'
    elif 5 < media < 6.5:
        situacao = 'Preocupante'
    elif media < 5:
        situacao = 'RUIM'
    resp = {'total': len(num), 'maior': maior, 'menor': menor, 'media': media, 'Situacao': situacao}
    return resp


resp = notas(3.2, 7.2, 2.5, 7.3, 0, 6.5, 3.1)
print(resp)

