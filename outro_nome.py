def norma(x: list[list[float]]) -> float:
    """Calcula a norma de uma matriz"""
    # TODO: implementar
    # a norma de uma matriz [[1, 2, 4], [2, 3, 4]] é 6.928203230275509
    # ela consiste em calcular a raiz quadrada da soma dos quadrados dos elementos da matriz
    # caso a matriz esteja vazia deve-se retornar 0
    quadrado = 0
    resultado = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            quadrado += j**2
            resultado = quadrado
    print(resultado**0.5)

matriz = [[1, 2, 4], [2, 3, 4]]
norma(matriz)