def parcela(valor, n):
    if n < 1 and n > 12:
        raise ValueError("parcelas invalidas")
    if n <= 3:
        juros = 0
    else:
        juros = 0.02 * (n - 3)
    total = valor * (1 + juros)
    return round(total / n, )

#b) Todos os ramos foram percorridos(4/4)
# MS = (26/27)*100 = 96.3%

#c) O único mutante vivo não é equivalente, pois ele trata caso de 3 parcelas como se tivesse juros. Porém no próprio cálculo de juros, o resultado será 0.
# MS depois = (26/26)*100 = 100%

#e) a suíte conseguiu matar o mutante de segunda ordem