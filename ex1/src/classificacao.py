def classificar_aluno(media, presenca):
    if media < 0 or media > 10:
        raise ValueError("Media invalida")
    if presenca < 0 or presenca > 100:
        raise ValueError("Presenca invalida")
    if presenca < 75:
        return "Reprovado por falta"
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"

    #a)Foram gerados 36 mutantes, todos vivos. Logo: MS = 0%

    #b)Os mutantes vivos se dividem nos seguintes grupos:
    # Mutantes que alteram os valores numéricos
    # Mutantes que alteram operadores lógicos
    # Mutantes que alteram operadores relacionais

    #c)Após todos os mutantes estarem mortos, o MS final é de 100%

    #d)Ao colocar essa condição, o teste passa a não só pegar um erro de valor, mas também ver se a mensagem dada pelo teste corresponde com o padrão informado