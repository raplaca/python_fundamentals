# -*- coding: utf-8 -*-

# dada a string 

# Não deixe o barulho da opinião dos outros abafar sua voz interior. 
# E mais importante, tenha a coragem de seguir seu coração e sua intuição.
# Eles de alguma forma já sabem o que você realmente quer se tornar. 
# Tudo o mais é secundário.



# conte quantas letras a tem no texto
# mude todas as letras o para s
# divida o texto em uma lista colocando virgulas nos espaços

# texto = "Não deixe o barulho da opinião dos outros abafar sua voz interior. \
# E mais importante, tenha a coragem de seguir seu coração e sua intuição. \
# Eles de alguma forma já sabem o que você realmente quer se tornar. \
# Tudo o mais é secundário."

# print(texto.count('a'))
# print(texto.replace('o', 's'))
# print(texto.split(' '))


#dada a lista abaixo:

# lista = ['Corinthians', [1, 2, 3, 4, 5] ,
#          'Palmeiras', 'São Paulo', 
#         [10, 11, 12, 13, 14],'Flamengo', 'Vasco']



# # print 3, 13, Vasco
# print(lista[1][2], lista[-3][-2], lista [-1])
# # print 5, São Paulo, 14
# print(lista[1][-1], lista[3], lista [-3][-1])
# # mude o valor de 4 para 40
# lista[1][-2] = 40
# # mude o valor de 14 para 150
# lista [-3][-1] = 150
# print(lista)



# dados = {

#     'cidades': {
#         'saopaulo': {
#             'nome': 'São Paulo',
#             'municipios': 645,
#             'população': 12.18
#         },
#         'riodejaneiro': {
#             'nome': 'Rio de Janeiro',
#             'municipios': 92,
#             'população': 6.32
#         },
#         'minasgerais': {
#             'nome': 'Minas Gerais',
#             'municipios': 31,
#             'população': 20.87

#         }
#     }
# }


# # imprima a quantiddade de municipios de minas

# print('Total de municipios de Minias Gerais: ' dados['cidades']['minasgerais']['municipios'])

# # imprima a quantidade de municipios do rio

# print(dados['cidades']['riodejaneiro']['municipios'])

# # imprima o nome e população de são paulo em milhoes

# print(dados['cidades']['saopaulo']['população'])


# imprima a quantiddade de municipios de minas

# imprima a quantidade de municipios do rio

# imprima o nome e população de são paulo em milhoes


# ['rafaela','luis', 'joao', 'ana', 'paulo', 'fernando', 'marilia', 'tarcisio', 'carlos', 'manuel']


# faça um for que imprima o nome de cada pessoa da lista e com a mensagem 'bem-vindo {}'

lista = ['rafaela','luis', 'joao', 'ana', 'paulo', 'fernando', 'marilia', 'tarcisio', 'carlos', 'manuel']

for nome in lista:
    print(f"Bem Vindo(a): {nome}")


