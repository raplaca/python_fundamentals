# def soma(x, y):
#     return x + y

# def subtrair(x, y):
#     return x - y

# def dividir(x, y):
#     return x / y

# def multiplicar(x, y):
#     return x * y

# assert soma(2, 2) == 4, f" Obtido: {soma(2,2)}, Esperado: 4"
# assert subtrair(2, 2) == 0, f"Obtido: {subtrair(2, 2)}, Esperado: 0"
# assert dividir (4, 2)  == 2, f"Obtido: {dividir(2, 2)}, Esperado: 2"
# assert multiplicar (10, 2)  == 20, f"Obtido: {multiplicar(2, 2)}, Esperado: 20"


# escrever um teste para a função maior

# def maior(*valores):
#     return max(valores)

# assert maior(2, 5, 150) == 150, f"Obtido: {maior(2, 5, 150)}, Esperado: 150"


## Unittest

from unittest import TestCase, main

def minimo(*valores):
    return min(valores)

class Testes(TestCase):
    def test_minimo(self):
        self