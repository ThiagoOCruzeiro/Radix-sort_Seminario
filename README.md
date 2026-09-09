
https://canva.link/yuubcdysqs59wgl

# Radix-sort_Seminario
Disponibilizamos o código, relação ao seminário.



Ideia geral do algoritmo

Radix Sort ordena números olhando um dígito de cada vez, começando pelo dígito menos significativo (unidade) até o mais significativo. Para ordenar por cada dígito, ele usa o Counting Sort como sub-rotina, porque o Counting Sort é estável (mantém a ordem relativa de elementos iguais) — isso é essencial para o Radix Sort funcionar corretamente.

Função counting_sort(arr, exp) (linhas 1-19)

Ordena a lista com base em um dígito específico, indicado pelo parâmetro exp (exp = 1 → unidade, exp = 10 → dezena, exp = 100 → centena...).

Linhas 2-4: cria a lista saida (vai guardar o resultado) e contagem, um array de 10 posições (dígitos de 0 a 9), tudo zerado.
Linhas 6-8: percorre o array original e, para cada número, extrai o dígito correspondente à posição atual usando (arr[i] // exp) % 10. Isso conta quantas vezes cada dígito (0-9) aparece.
Linhas 10-11: transforma a contagem em soma acumulada — assim contagem[i] passa a indicar a posição final onde o último elemento com aquele dígito deve ficar na saída.
Linhas 13-16: percorre o array de trás para frente (isso garante a estabilidade) e usa a contagem acumulada para colocar cada elemento na posição correta em saida, decrementando o contador depois de usá-lo.
Linhas 18-19: copia o resultado de volta para o array original.
Função radix_sort_positivos(arr) (linhas 22-30)

Aplica o counting_sort repetidamente, dígito por dígito, só que assumindo que todos os números são positivos.

Linha 23-24: se a lista estiver vazia, não faz nada.
Linha 25: encontra o maior número da lista, para saber quantos dígitos no máximo precisa processar.
Linha 26: começa com exp = 1 (dígito das unidades).
Linhas 28-30: enquanto ainda houver dígitos a processar (maior // exp > 0), chama o counting sort para aquele dígito e multiplica exp por 10 para avançar pro próximo dígito (dezena, centena, etc.).
Função radix_sort(arr) (linhas 33-41)

O Radix Sort "puro" só funciona com números não-negativos. Essa função é uma adaptação para lidar com números negativos:

Linhas 34-35: separa a lista em dois grupos — negativos (invertendo o sinal, ou seja, viram positivos) e positivos (incluindo o zero).
Linhas 37-38: ordena cada grupo separadamente usando o radix_sort_positivos.
Linha 40: devolve o sinal negativo aos números do primeiro grupo e inverte a ordem deles com reversed() — porque, por exemplo, -2 é maior que -45, então depois de ordenar como positivos (2, 45) e devolver o sinal, precisa inverter para ficar (-45, -2).
Linha 41 (cortada na imagem, mas é return negativos + positivos): junta os negativos (do mais negativo pro menos negativo) com os positivos ordenados normalmente, formando o resultado final.
Teste (linhas 45-47)

Cria uma lista de exemplo com números positivos e negativos, chama radix_sort e imprime o resultado ordenado.

Pontos-chave para destacar na apresentação
Complexidade: O(d × (n + k)), onde d é o número de dígitos do maior número, n é a quantidade de elementos e k é a base (10, no caso).
Por que Counting Sort: precisa ser estável para o Radix Sort funcionar.
Vantagem: não faz comparações diretas entre elementos (diferente de quicksort/mergesort), pode ser mais rápido em certos casos.
Limitação resolvida aqui: Radix Sort tradicional só ordena números não-negativos; o código contorna isso separando negativos e positivos.
