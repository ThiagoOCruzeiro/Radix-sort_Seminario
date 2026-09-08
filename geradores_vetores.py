"""
Secao 10 - Caracteristicas dos dados de entrada
Geracao dos diferentes tipos de vetores exigidos pelo enunciado.
Semente fixa (random.seed) para reprodutibilidade (Secao 12).
"""
import random


SEED = 42


def vetor_ordenado(n):
    """10.1 - Vetor ja ordenado crescente: [1, 2, 3, ..., n]"""
    return list(range(1, n + 1))


def vetor_reverso(n):
    """10.2 - Vetor em ordem totalmente reversa: [n, n-1, ..., 1]"""
    return list(range(n, 0, -1))


def vetor_aleatorio(n, limite_superior=None):
    """10.3 - Vetor com elementos distribuidos pseudoaleatoriamente."""
    random.seed(SEED)
    if limite_superior is None:
        limite_superior = n * 10
    return [random.randint(0, limite_superior) for _ in range(n)]


def vetor_parcialmente_desordenado(n, percentual_desordem):
    """
    10.4 - Vetor parcialmente desordenado.
    Metodologia: parte-se do vetor ordenado e embaralha-se apenas uma
    fracao dos elementos (percentual_desordem), trocando pares de posicoes
    escolhidas aleatoriamente. Isso simula diferentes graus de desordem
    (10%, 25%, 50%, 75%) mantendo o restante do vetor na ordem original.
    """
    random.seed(SEED)
    arr = list(range(1, n + 1))
    qtd_trocas = int((n * percentual_desordem) / 2)  # cada troca desordena 2 posicoes
    for _ in range(qtd_trocas):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def vetor_com_repetidos(n, qtd_valores_distintos=None):
    """
    10.5 - Vetor com elementos repetidos.
    Metodologia: gera valores sorteados a partir de um conjunto reduzido
    de valores distintos (qtd_valores_distintos), forcando repeticao.
    Por padrao usa n // 10 valores distintos (ou no minimo 5), ou seja,
    em media cada valor se repete ~10 vezes.
    """
    random.seed(SEED)
    if qtd_valores_distintos is None:
        qtd_valores_distintos = max(5, n // 10)
    return [random.randint(0, qtd_valores_distintos) for _ in range(n)]


TIPOS_DE_ENTRADA = {
    "ordenado": lambda n: vetor_ordenado(n),
    "reverso": lambda n: vetor_reverso(n),
    "aleatorio": lambda n: vetor_aleatorio(n),
    "desordem_10pct": lambda n: vetor_parcialmente_desordenado(n, 0.10),
    "desordem_25pct": lambda n: vetor_parcialmente_desordenado(n, 0.25),
    "desordem_50pct": lambda n: vetor_parcialmente_desordenado(n, 0.50),
    "desordem_75pct": lambda n: vetor_parcialmente_desordenado(n, 0.75),
    "com_repetidos": lambda n: vetor_com_repetidos(n),
}


if __name__ == "__main__":
    n = 10
    for nome, gerador in TIPOS_DE_ENTRADA.items():
        print(f"{nome:18s}: {gerador(n)}")
