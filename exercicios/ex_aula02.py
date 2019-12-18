## Entrada e saída de dados

# Crie um programa que peça um número e multiplique por 15

# numero = int(input('Digite um numero: '))

# print(f'O numero digitado foi: {numero}' f' Multiplicado por 15 é: {(numero * 15)}')

# Repetição 
# Multiplique os numeros da lista por 15
# e coloque o resultado na lista multiplicados

# numeros = [1, 2, 3, 4, 5, 6]
# multiplicados = []

# for numero in numeros:
#     multiplicados.append(numero * 15)

# print(multiplicados)

### ou na forma reduzida

# numeros = [1, 2, 3, 4, 5, 6]

# multiplicado = [i*15 for i in numeros]
# print(multiplicado)

# usuarios = ['ana', 'bruno', 'caio', 'camila', 'joao']

# Peça para o usuario digitar o seu nome e caso não
# esteja na lista print um erro

# fazer um sistema que pergunte o sexo do usuario sendo, M, F
# mostre se o usuario é do sexo masculino ou feminino.

# print('Digite seu sexo')
# print('M - para Masculino')
# print('F - para Feminino')

# while True:
#     user = input('>>> ')
#      if user.lower() == 'm':
#         print('Usuario de sexo masculino')
#         break
#     elif user.lower() == 'f':
#         print('Usuario do sexo feminino')
#         break
#     else:
#         print('Entrada Invalida, Digite novamente! ')
#         continue

############                  ###################

# usuarios = ['ana', 'bruno', 'caio', 'camila', 'joao']

# Peça para o usuario digitar o seu nome e caso não
# esteja na lista print um erro "Usuariio não cadastrado"


# try:
#         usuarios = ['ana', 'bruno', 'caio', 'camila', 'joao']
#         usuario = str(input('Digite seu nome: '))
#         if usuario.lower() not in usuarios:
#             raise NameError('Usuario não cadastrado')
#         else:
#             print(f'Login efetuado! {usuario}')
# except NameError as n:
#     print(n)