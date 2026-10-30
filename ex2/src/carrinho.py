def total_com_desconto(precos):
    total = 0
    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.9
        else:
            total += preco
    return round(total, 2)

#a) MS = (4/16)*100 = 25%. Os numeros dizem que 25% dos mutantes morrem no teste

#b) Após a troca, restam apenas 3 mutantes vivos

#c) Os 3 mutantes vivos falharam na condição de Infectar, onde a alteração do resultado não teve diferença no estado interno do código

#d) Foi preciso colocar números com, pelo menos, 3 casas decimais para que a função de arredondamento do código faça efeito sobre os mutantes vivos