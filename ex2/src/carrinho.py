def total_com_desconto(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.9
        else:
            total += preco
    return round(total, 2)

#a) MS = (4/16)*100 = 25%. Os numeros dizem que 25% dos mutantes morrem no teste

#b) 