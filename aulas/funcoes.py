# -*- coding: utf-8 -*-


# def printa_nome(nome):
#     print(nome)



# printa_nome('Roberto')

##### Outro Exemplo

# carrinho = []
# produto1 = dict(nome="Tenis", valor=21.70)
# produto2 = dict(nome="Meia", valor=10)
# produto3 = dict(nome="Camiseta", valor=17.30)
# produto4 = dict(nome="Calca", valor=100.00)
# carrinho.append(produto1)
# carrinho.append(produto2)
# carrinho.append(produto3)
# carrinho.append(produto4)

# def totalCarrinho(carrinho):
#     return sum(produto["valor"] for produto in carrinho)


# def cupomDesconto(cupom=""):
#     if cupom == "xzygratis":
#         return 0.50
#     else:
#         return 1

# print("O valor da sua compra é: ",
#  (totalCarrinho(carrinho)* cupomDesconto()))


# print("Utilizando o cupom xzygratis o valor será de ",
#             totalCarrinho(carrinho) * cupomDesconto("xzygratis"))


# Faça 4 funções:
    # 1 para somar dois valores
    # 1 para subtrair dois valores
    # 1 para dividir dois valores
    # 1 para multiplicar dois valores

# def somar(valor1, valor2):
#     print(valor1 + valor2)

# somar(1,2)

# def subtrair(valor1, valor2):
#     print(valor1 - valor2)

# subtrair(7,5)

# def dividir(valor1, valor2):
#     print(valor1 / valor2)

# dividir(10,5)

# def multiplicar(valor1, valor2):
#     print(valor1 * valor2)

# multiplicar(5,8)







servidor = "192.168.0.2"

def classe_a():
    servidor = "192.168.0.1"

def classe_b():
    print(servidor)

if _name_ ==  