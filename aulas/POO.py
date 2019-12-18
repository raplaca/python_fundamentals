# -*- coding: utf-8 -*-

"""
orientação ao objeto
classes!!!!

POO

Abstração

Entidades  ## Generalização
atributos  ## Caracteristicas
Métodos    ## Ações
Instâncias ## Um exemplar de uma entidade
"""
# class Passaros():

#     def __init__(self): ## metodo construtor
#         self.asas = 2           ## atributos
#         self.penas = True
#         self.bico = True
#         self.patas = 2

#     def voar(self):
#         if self.asas < 2:
#             self.cont = 0
#             print('Passaros deficiente!')  ## Metodos -- Ações
#             print('Não pode voar')  ## Metodos -- Ações
#         else:
#             self.cont = 1
#             print('Passaros deficiente!')  ## Metodos -- Ações


#     def pousar(self):
#         if self.cont == 0:
#             pass
#         else:
#             print('Pousando...')  ## Metodos -- Ações

#     def comer(self):
#         print('Comendo...')  ## Metodos -- Ações

#     def dormir(self):
#         print('Dormindo...')  ## Metodos -- Ações

# sabia = Passaros()
# sabia.asas = 1 ## Modificou o atributo somente no sabia não na classe
# sabia.voar()
# print(sabia.asas)

# codorna = Passaros()
# ##print(f'numero de asas da codorna: {codorna.asas}')
# print(codorna.asas)

# class Servidor():
#     def __init__(self, cpu, memoria, disco):
#         self.cpu = cpu
#         self.memoria = memoria
#         self.disco = disco

# servidorWEB = Servidor("2 vcpus", "16GB", "50GB")

# print(servidorWEB.cpu)
# print(servidorWEB.memoria)
# print(servidorWEB.disco)


# class Servidor():
#     def __init__(self):
#         self.cpu = 2
#         self.memoria = 2048
#         self.disco = 500
    
#     def inserirMemoria(self, mem):
#         self.memoria += mem

#     def inserirCpu(self, cpu):
#         self.cpu += cpu

#     def inserirDisco(self, hd):
#         self.dico += hd

#     def removeMemoria(self, mem):
#         self.memoria -= mem

        
#     def removeCpu(self, cpu):
#         self.cpu -= cpu

#     def removeDisco(self, hd):
#         self.disco -= hd

# servidorWEB = Servidor()

# print(servidorWEB)
# servidorWEB.inserirMemoria(1024)
# print(servidorWEB.memoria)
# print(servidorWEB.disco)

# servidorDNS = Servidor()
# print(servidor)
# servidorWEB.removeMemoria(1024)
# print(removeMemoria)