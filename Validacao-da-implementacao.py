def esta_ordenado(vetor):
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            return False
    return True


# Testes
testes = [
    [5, 2, 8, 1, 4],
    [],
    [7],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [3, 1, 3, 2],
    [-2, 5, -1, 0],
    [2, 2, 2]
]

for vetor in testes:
    print(vetor, "->", esta_ordenado(vetor))