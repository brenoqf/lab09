def maior(temps):
    if not temps:
        raise ValueError("lista vazia")
    m = temps[0]
    for t in temps[1:]:
        if t > m:
            m = t
    return m

def dia_do_maior(temps):
    if not temps:
        raise ValueError("lista vazia")
    pos = 0
    for i in range(1, len(temps)):
        if temps[i] > temps[pos]:
            pos = i
    return pos

#a) def maior:
# temperaturas.x_maior__mutmut_2: survived
# --- src/temperaturas.py
# +++ src/temperaturas.py
# @@ -1,6 +1,6 @@
#  def maior(temps):
#      if not temps:
# -        raise ValueError("lista vazia")
# +        raise ValueError(None)
#      m = temps[0]
#      for t in temps[1:]:
#          if t > m:
# # temperaturas.x_maior__mutmut_3: survived
# --- src/temperaturas.py
# +++ src/temperaturas.py
# @@ -1,6 +1,6 @@
#  def maior(temps):
#      if not temps:
# -        raise ValueError("lista vazia")
# +        raise ValueError("XXlista vaziaXX")
#      m = temps[0]
#      for t in temps[1:]:
#          if t > m:
# # temperaturas.x_maior__mutmut_4: survived
# --- src/temperaturas.py
# +++ src/temperaturas.py
# @@ -1,6 +1,6 @@
#  def maior(temps):
#      if not temps:
# -        raise ValueError("lista vazia")
# +        raise ValueError("LISTA VAZIA")
#      m = temps[0]
#      for t in temps[1:]:
#          if t > m:
# # temperaturas.x_maior__mutmut_7: survived
# --- src/temperaturas.py
# +++ src/temperaturas.py
# @@ -2,7 +2,7 @@
#      if not temps:
#          raise ValueError("lista vazia")
#      m = temps[0]
# -    for t in temps[1:]:
# +    for t in temps[2:]:
#          if t > m:
#              m = t
#      return m
# # temperaturas.x_maior__mutmut_8: survived
# --- src/temperaturas.py
# +++ src/temperaturas.py
# @@ -3,6 +3,6 @@
#          raise ValueError("lista vazia")
#      m = temps[0]
#      for t in temps[1:]:
# -        if t > m:
# +        if t >= m:
#              m = t
#      return m

# def dia_do_maior:
# temperaturas.x_dia_do_maior__mutmut_2: survived
# --- src/temperaturas.py
# +++ src/temperaturas.py
# @@ -1,6 +1,6 @@
#  def dia_do_maior(temps):
#      if not temps:
# -        raise ValueError("lista vazia")
# +        raise ValueError(None)
#      pos = 0
#      for i in range(1, len(temps)):
#          if temps[i] > temps[pos]:
# # temperaturas.x_dia_do_maior__mutmut_3: survived
# --- src/temperaturas.py
# +++ src/temperaturas.py
# @@ -1,6 +1,6 @@
#  def dia_do_maior(temps):
#      if not temps:
# -        raise ValueError("lista vazia")
# +        raise ValueError("XXlista vaziaXX")
#      pos = 0
#      for i in range(1, len(temps)):
#          if temps[i] > temps[pos]:
# # temperaturas.x_dia_do_maior__mutmut_4: survived
# --- src/temperaturas.py
# +++ src/temperaturas.py
# @@ -1,6 +1,6 @@
#  def dia_do_maior(temps):
#      if not temps:
# -        raise ValueError("lista vazia")
# +        raise ValueError("LISTA VAZIA")
#      pos = 0
#      for i in range(1, len(temps)):
#          if temps[i] > temps[pos]:
# # temperaturas.x_dia_do_maior__mutmut_6: survived
# --- src/temperaturas.py
# +++ src/temperaturas.py
# @@ -1,7 +1,7 @@
#  def dia_do_maior(temps):
#      if not temps:
#          raise ValueError("lista vazia")
# -    pos = 0
# +    pos = 1
#      for i in range(1, len(temps)):
#          if temps[i] > temps[pos]:
#              pos = i
# # temperaturas.x_dia_do_maior__mutmut_9: survived
# --- src/temperaturas.py
# +++ src/temperaturas.py
# @@ -2,7 +2,7 @@
#      if not temps:
#          raise ValueError("lista vazia")
#      pos = 0
# -    for i in range(1, len(temps)):
# +    for i in range(len(temps)):
#          if temps[i] > temps[pos]:
#              pos = i
#      return pos
# # temperaturas.x_dia_do_maior__mutmut_10: survived
# --- src/temperaturas.py
# +++ src/temperaturas.py
# @@ -2,7 +2,7 @@
#      if not temps:
#          raise ValueError("lista vazia")
#      pos = 0
# -    for i in range(1, len(temps)):
# +    for i in range(1, ):
#          if temps[i] > temps[pos]:
#              pos = i
#      return pos
# # temperaturas.x_dia_do_maior__mutmut_11: survived
# --- src/temperaturas.py
# +++ src/temperaturas.py
# @@ -2,7 +2,7 @@
#      if not temps:
#          raise ValueError("lista vazia")
#      pos = 0
# -    for i in range(1, len(temps)):
# +    for i in range(2, len(temps)):
#          if temps[i] > temps[pos]:
#              pos = i
#      return pos
# # temperaturas.x_dia_do_maior__mutmut_12: survived
# --- src/temperaturas.py
# +++ src/temperaturas.py
# @@ -3,6 +3,6 @@
#          raise ValueError("lista vazia")
#      pos = 0
#      for i in range(1, len(temps)):
# -        if temps[i] > temps[pos]:
# +        if temps[i] >= temps[pos]:
#              pos = i
#      return pos

#b) MAIOR()
# mutantes 2, 3, 4 não são equivalentes, pois todos envolvem a não verificação de mensagem do ValueError
# mutante 7 não é equivalente, pois ele ainda dá como resposta o 30
# mutante 8 é equivalente, pois ele altera o operador lógico no segundo if que, nesse caso, não muda o resultado

# DIA_DO_MAIOR()
# mutante 2, 3, 4 não são equivalentes, pois todos envolvem a não verificação de mensagem do ValueError
# mutante 6 não é equivalente, pois a troca de posição pode ser detectada por um vetor de um único valor
# mutante 9 é equivalente, pois o laço de repetição começa com 0 elementos, assim a comparação é feita entre ele mesmo
# mutante 10 não é equivalente, pois o laço não possui um limite determinado
# mutante 11 não é equivalente, pois o laço começa a comparar com o segundo elemento, ao inves do primeiro
# mutante 12 não é equivalente, pois altera o operador lógico de determinar o maior valor

#c) MS antes = (13/22)*100 = 59,1%
# MS depois = (20/22)*100 = 90,9%

#d) Porque essa troca na função "maior()" não altera o resultado final, já que ela retorna apenas o maior valor da lista. Assim, mesmo tendo dois valores iguais, o resultado será o mesmo.
# Já na função "dia_do_maior()" altera o funcionamento do código, pois ela vê a posição que o maior valor apareceu. Com essa alteração, se houver valores iguais, o programa passa a mostrar a posição de todos os maiores valores.