"""
Radix Sort - implementacao base (mesmo do radixsort2(1))
Instrumentada para contar operacoes relevantes (iteracoes e movimentacoes),
que sao as metricas aplicaveis ao Radix Sort (ele nao faz comparacoes
nem trocas no sentido classico, pois usa contagem/distribuicao).
"""


class Contador:
    """Guarda as metricas de uma execucao do radix sort."""
    def __init__(self):
        self.iteracoes = 0        # passagens pelos digitos (loops de exp)
        self.movimentacoes = 0    # escritas no vetor de saida / contagem
        self.acessos = 0          # leituras de arr[i] (proporcional ao trabalho)


def counting_sort(arr, exp, contador):
    n = len(arr)
    saida = [0] * n
    contagem = [0] * 10

    for i in range(n):
        digito = (arr[i] // exp) % 10
        contagem[digito] += 1
        contador.acessos += 1

    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    for i in range(n - 1, -1, -1):
        digito = (arr[i] // exp) % 10
        saida[contagem[digito] - 1] = arr[i]
        contagem[digito] -= 1
        contador.movimentacoes += 1

    for i in range(n):
        arr[i] = saida[i]
        contador.movimentacoes += 1


def radix_sort_positivos(arr, contador):
    if not arr:
        return
    maior = max(arr)
    exp = 1

    while maior // exp > 0:
        counting_sort(arr, exp, contador)
        contador.iteracoes += 1
        exp *= 10


def radix_sort(arr, contador=None):
    """
    separa negativos e positivos,
    ordena cada parte com radix (baseado em contagem por digito)
    e depois junta os negativos invertidos com os positivos.
    """
    if contador is None:
        contador = Contador()

    negativos = [-n for n in arr if n < 0]
    positivos = [n for n in arr if n >= 0]

    radix_sort_positivos(negativos, contador)
    radix_sort_positivos(positivos, contador)

    negativos = [-n for n in reversed(negativos)]

    return negativos + positivos, contador


if __name__ == "__main__":
    numeros = [170, -45, 75, -90, 802, 24, -2, 66]
    resultado, c = radix_sort(numeros)
    print(resultado)
    print(f"Iteracoes: {c.iteracoes}, Movimentacoes: {c.movimentacoes}")
