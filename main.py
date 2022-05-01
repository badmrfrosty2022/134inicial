import pytest

def imprimir_oi(nome):
    print(f'Oi, {nome}')

def somar(numero_a, numero_b):
    return numero_a + numero_b

if __name__ == '__main__':
    imprimir_oi('Edu')

    resultado = somar(5, 7)
    print (f'A soma: {resultado}')

def teste_somar():
    #1 - Configura
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    #2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    #3 - Valida
    assert resultado_obtido == resultado_esperado