# -*- coding: utf-8 -*-


# Crie uma classe automovel, com os atributos:
#                             Motor
#                             Marca
#                             Ano
#                             Preco

# e com os métodos que retornam o valor de:
#                                         Motor
#                                         Marca
#                                         Ano
#                                         Preco


# class Automovel():

#     def __init__(self, motor, marca, ano, preco):
#         self.motor = motor
#         self.marca = marca
#         self.ano = ano
#         self.preco = preco

#     def get_motor(self):
#         print(self.motor)

#     def get_marca(self):
#         print(self.marca)

#     def set_marca(self, marca):
#         self.marca = marca

#     def get_ano(self):
#         print(self.ano)


#     @property
#     def preco(self):
#         return self._preco

#     @preco.setter
#     def preco(self, new_preco):
#         self._preco = new_preco
    
#     @preco.getter
#     def getpreco(self):
#         self._preco


# Crie uma classe automovel, com os atributos:
#                             Motor
#                             Marca
#                             Ano
#                             Preco

# e com os métodos que retornam o valor de:
#                                         Motor
#                                         Marca
#                                         Ano
#                                         Preco

"""
We are all consenting adults (algo como “somos todos adultos responsáveis”, 
significando que a linguagem não precisa ficar cercando o programador como se ele 
fosse criança)
"""



# class Automovel():

#     def __init__(self, motor, marca, ano, preco):
#         self.motor = motor
#         self.marca = marca
#         self.ano = ano
#         self.preco = preco

#     def get_motor(self):
#         print(self.motor)

#     def get_marca(self):
#         print(self.marca)

#     def get_ano(self):
#         print(self.ano)

#     @property
#     def preco(self):
#         return self._preco

#     @preco.setter
#     def preco(self, new_preco):
#         self._preco = new_preco
    

#     def get_preco(self):
#         print(self._preco)

# class Moto(Automovel):

#     def __init__(self, motor, marca, ano, preco, tipo='Moto'):
#         super().__init__(motor, marca, ano, preco)
#         self.rodas = 2

#     def ligar(self):
#         print('Ligada...')
    
#     def desligar(self):
#         print('Desligando...')
#         print( 'Desligada...')

#     def acelerar(self):
#         print('Acelerando...')
    
#     def frear(self):
#         print('Freando...')



# if __name__ == "__main__":
#     CB500 = Moto('500CC', 'Honda', 2017, 35000)
#     CB500.get_ano()
#     CB500.get_marca()
#     CB500.get_preco()
#     CB500.preco = 20000
#     CB500.get_preco()


# class Base():
#     def __init__(self):
#         print('Contrutor da classe Base')
    

# class Derivada(Base):
#     def __init__(self):
#         Base.__init__(self)
#         # super().__init__()
#         # print('Contrutor da classe Derivada')


# # base = Base()

# derivada = Derivada()








# Faça uma classe de uma conta bancaria que tera os seguintes 
# atributos:
            # Nome do banco  Oldbak    
#            Número do banco    99
            # Número da agencia   
            # número da conta
            # nome do cliente
            # saldo


# métodos:
#         Sacar
#         Depositar
#         Extrato


# Menu

# 1 - para saque
# 2 - deposito
# 3 - extrato


# Extrato

# Nome do Banco
#====================
# Clinte: tal
# Conta: tal Ag: ta
#  Saldo

# Faça uma classe de uma conta bancaria que tera os seguintes 
# atributos:
            # Nome do banco  Oldbak    
#            Número do banco    99
            # Número da agencia   
            # número da conta
            # nome do cliente
            # saldo


# métodos:
#         Sacar
#         Depositar
#         Extrato


# Menu

# 1 - para saque
# 2 - deposito
# 3 - extrato


# Extrato

# Nome do Banco
#====================
# Clinte: tal
# Conta: tal Ag: ta
#  Saldo


class Oldbank():

    def __init__(self, cl, cc, ag, sld=0, banco='OldBank', num_banco=99):
        self.cliente = cl
        self.conta = cc
        self.agencia = ag
        self.saldo = sld
        self.banco = banco
        self.n_banco = num_banco

    def deposito(self):
        print(f'Saldo atual: {self.saldo}')
        print('=' * 15)
        deposito = float(input('Digite o valor a ser depositado: '))
        print(f'Valor depositado (+) {deposito}')
        self.saldo += deposito
        print(f'Novo Saldo: {self.saldo}')
    
    def saque(self):
        print(f'Saldo atual: {self.saldo}')
        print('=' * 15)
        saque = float(input('Digite o valor a ser sacado: '))
        if self.saldo < saque:
            print('Saldo insuficiente! ')
        else:
            self.saldo -= saque
            print(f'Novo Saldo: {self.saldo}')
        
    def extrato(self):
        print('EXTRATO')
        print('')
        print('Old Bank')
        print('='* 15)
        print('Cliete: ', self.cliente)
        print('Conta: ', self.conta,'Ag:', self.agencia)
        print('Saldo:', self.saldo)
    







