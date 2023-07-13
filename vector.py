"""Módulo com as funções de manipulação de vetores."""
from tipos import Escalar, Matriz, Vetor


def norma(x: Vetor) -> float | None:
    """Calcula a norma de um vetor"""
    # a norma de um vetor [3, 4] é 5
    # a norma de um vetor [1, 2, 4] é 4.58257569495584
    # ela consiste em calcular a raiz quadrada da soma dos quadrados dos elementos do vetor
    # se o vetor estiver vazio retorne None
    if len(x) == 0:
        return None
    soma_norma = 0
    for elemento in x:
        soma_norma += elemento**2
    return soma_norma**0.5


def soma(x: Vetor, y: Vetor) -> Vetor | None:
    """Soma dois vetores"""
    # a soma de dois vetores [1, 2, 4] + [2, 3, 4] é [3, 5, 8]
    # a soma só pode ser realizada se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None
    if len(x) == len(y):
        soma_vetor = []
        for i, _ in enumerate(x):
            soma_vetor.append(x[i] + y[i])
        return soma_vetor
    return None


def multiplicacao_por_escalar(vetor: Vetor, escalar: Escalar) -> Vetor:
    """Multiplica um vetor por um escalar"""
    # a multiplicacao de um vetor [1, 2, 4] por um escalar 2 é [2, 4, 8]
    mult = []
    for i in vetor:
        mult.append(i * escalar)
    return mult


def produto_interno(x: Vetor, y: Vetor) -> Escalar | None:
    """Calcula o produto interno de dois vetores"""
    # o produto interno de dois vetores [1, 2, 4] e [2, 3, 4] é 24
    # o produto interno consiste em multiplicar os elementos de mesmo índice e somar os resultados
    # a multiplicacao só pode ser realizada se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None
    # caso os vetores sejam vazios o resultado é 0
    if len(x) == len(y):
        soma_prod = 0
        for i, _ in enumerate(x):
            soma_prod += x[i] * y[i]
        return soma_prod
    return None


def produto_vetorial(x: Vetor, y: Vetor) -> Vetor | None:
    """Calcula o produto vetorial de dois vetores"""
    # o produto vetorial de dois vetores [1, 2, 4] e [2, 3, 4] é [-4, 4, -1]
    # o produto vetorial só pode ser realizado se os vetores tem 3 elementos.
    # caso contrário, deve retornar None
    if len(x) == 3 and len(y) == 3:
        vetor = [
            x[1] * y[2] - x[2] * y[1],
            x[2] * y[0] - x[0] * y[2],
            x[0] * y[1] - x[1] * y[0],
        ]
        return vetor
    return None


def produto_diadico(x: Vetor, y: Vetor) -> Matriz | None:
    """Calcula o produto diádico de dois vetores"""
    # o produto diádico de dois vetores [1, 2, 4] e [2, 3, 4] é [[2, 3, 4], [4, 6, 8], [8, 12, 16]]
    # o produto diádico só pode ser realizado se os vetores tem a mesma quantidade de elementos.
    # caso contrário, deve retornar None
    if len(x) == len(y):
        resultado = []
        for _, valor_x in enumerate(x):
            linha_res = []
            for _, valor_j in enumerate(y):
                linha_res.append(valor_x * valor_j)
            resultado.append(linha_res)
        return resultado
    return None