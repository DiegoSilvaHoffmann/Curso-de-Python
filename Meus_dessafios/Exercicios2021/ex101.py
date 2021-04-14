def voto(ano):
    from datetime import date
    a = date.today().year
    s = a - nasc
    if 18 < s < 65:
        return f'Com {s} anos voto é OBRIGATORIO!'
    elif s < 18:
        return f'Tem {s} anos, e NAO vota!'
    elif s >= 65:
        return f'Tem {s}anos e o voto é OPCIONAL.'


nasc = int(input('Qual a sua data de nascimento: '))
print(voto(nasc))
