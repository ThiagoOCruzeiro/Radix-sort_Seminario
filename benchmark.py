"""
PESSOA 4 - Ambiente Experimental e Benchmarks (Secoes 8 a 12)
==============================================================

Este script:
  - Secao 8:  mede tempo de execucao, iteracoes e movimentacoes (metricas
              aplicaveis ao Radix Sort - ele nao usa comparacoes/trocas
              classicas, e sim contagem e redistribuicao por digito).
  - Secao 9:  roda os benchmarks em tamanhos crescentes (10^1 a 10^5).
  - Secao 10: usa os 8 tipos de vetores de entrada exigidos.
  - Secao 11: repete cada configuracao 5x e calcula media/mediana/desvio.
  - Secao 12: fixa semente aleatoria e registra o ambiente de execucao.

Saida:
  - resultados_benchmark.csv  -> tabela bruta com todas as execucoes
  - resultados_resumo.csv     -> tabela agregada (media, mediana, desvio)
  - graficos/*.png            -> graficos tempo/iteracoes vs tamanho da entrada
"""
import time
import platform
import statistics
import csv
import sys
import tracemalloc

from radix_sort_base import radix_sort
from geradores_vetores import TIPOS_DE_ENTRADA


# ---------------------------------------------------------------------------
# Secao 12 - Controle experimental: registro do ambiente
# ---------------------------------------------------------------------------
def registrar_ambiente():
    info = {
        "sistema_operacional": platform.platform(),
        "versao_python": sys.version.split()[0],
        "processador": platform.processor() or "nao identificado",
    }
    return info


# ---------------------------------------------------------------------------
# Secao 16 (apoio) - Validacao: confere se o resultado esta corretamente ordenado
# ---------------------------------------------------------------------------
def esta_ordenado(vetor):
    return all(vetor[i] <= vetor[i + 1] for i in range(len(vetor) - 1))


# ---------------------------------------------------------------------------
# Secao 8 - Execucao unica com medicao de metricas
# ---------------------------------------------------------------------------
def executar_uma_vez(vetor_original):
    vetor = vetor_original.copy()

    tracemalloc.start()
    inicio = time.perf_counter()

    resultado, contador = radix_sort(vetor)

    fim = time.perf_counter()
    _, pico_memoria = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tempo_execucao = fim - inicio
    memoria_kb = pico_memoria / 1024

    ordenado_corretamente = esta_ordenado(resultado)

    return {
        "tempo_s": tempo_execucao,
        "iteracoes": contador.iteracoes,
        "movimentacoes": contador.movimentacoes,
        "acessos": contador.acessos,
        "memoria_kb": memoria_kb,
        "ordenado_corretamente": ordenado_corretamente,
    }


# ---------------------------------------------------------------------------
# Secao 11 - Repeticao dos experimentos (5x por configuracao)
# ---------------------------------------------------------------------------
def executar_repeticoes(vetor_original, repeticoes=5):
    execucoes = [executar_uma_vez(vetor_original) for _ in range(repeticoes)]

    tempos = [e["tempo_s"] for e in execucoes]
    todos_ordenados = all(e["ordenado_corretamente"] for e in execucoes)

    resumo = {
        "tempo_medio_s": statistics.mean(tempos),
        "tempo_mediana_s": statistics.median(tempos),
        "tempo_desvio_padrao_s": statistics.stdev(tempos) if len(tempos) > 1 else 0.0,
        "tempo_min_s": min(tempos),
        "tempo_max_s": max(tempos),
        "iteracoes": execucoes[0]["iteracoes"],          # deterministico, nao varia
        "movimentacoes": execucoes[0]["movimentacoes"],  # deterministico, nao varia
        "acessos": execucoes[0]["acessos"],               # deterministico, nao varia
        "memoria_kb_media": statistics.mean(e["memoria_kb"] for e in execucoes),
        "ordenado_corretamente": todos_ordenados,
    }
    return resumo


# ---------------------------------------------------------------------------
# Secao 9 - Benchmarks em escala crescente
# ---------------------------------------------------------------------------
TAMANHOS = [10, 100, 1_000, 10_000, 100_000]  # ate 10^5, conforme definido
REPETICOES = 5


def rodar_benchmarks():
    resultados = []

    print("Iniciando benchmarks do Radix Sort...")
    print(f"Tamanhos testados: {TAMANHOS}")
    print(f"Repeticoes por configuracao: {REPETICOES}")
    print(f"Tipos de entrada: {list(TIPOS_DE_ENTRADA.keys())}\n")

    total = len(TAMANHOS) * len(TIPOS_DE_ENTRADA)
    contagem_atual = 0

    for n in TAMANHOS:
        for nome_tipo, gerador in TIPOS_DE_ENTRADA.items():
            contagem_atual += 1
            vetor = gerador(n)

            resumo = executar_repeticoes(vetor, repeticoes=REPETICOES)
            resumo["n"] = n
            resumo["tipo_entrada"] = nome_tipo
            resultados.append(resumo)

            status = "OK" if resumo["ordenado_corretamente"] else "FALHOU"
            print(
                f"[{contagem_atual}/{total}] n={n:>7} | {nome_tipo:16s} | "
                f"tempo_medio={resumo['tempo_medio_s']:.6f}s | "
                f"iteracoes={resumo['iteracoes']} | ordenacao={status}"
            )

    return resultados


def salvar_csv(resultados, caminho):
    campos = [
        "n", "tipo_entrada",
        "tempo_medio_s", "tempo_mediana_s", "tempo_desvio_padrao_s",
        "tempo_min_s", "tempo_max_s",
        "iteracoes", "movimentacoes", "acessos",
        "memoria_kb_media", "ordenado_corretamente",
    ]
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for r in resultados:
            writer.writerow(r)
    print(f"\nCSV salvo em: {caminho}")


if __name__ == "__main__":
    ambiente = registrar_ambiente()
    print("=== Ambiente de execucao (Secao 12) ===")
    for chave, valor in ambiente.items():
        print(f"{chave}: {valor}")
    print()

    resultados = rodar_benchmarks()
    salvar_csv(resultados, "resultados_benchmark.csv")

    todos_ok = all(r["ordenado_corretamente"] for r in resultados)
    print(f"\nValidacao geral: {'TODOS OS TESTES ORDENARAM CORRETAMENTE' if todos_ok else 'HOUVE FALHA EM ALGUM TESTE'}")
