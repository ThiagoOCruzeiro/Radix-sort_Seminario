"""
Secao 13 - Graficos
Le resultados_benchmark.csv e gera os graficos de tempo e iteracoes
versus tamanho da entrada, um por tipo de entrada (todos sobrepostos).
"""
import csv
import os
import matplotlib.pyplot as plt

PASTA_SAIDA = "graficos"
os.makedirs(PASTA_SAIDA, exist_ok=True)


def carregar_resultados(caminho="resultados_benchmark.csv"):
    dados = {}
    with open(caminho, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for linha in reader:
            tipo = linha["tipo_entrada"]
            n = int(linha["n"])
            tempo = float(linha["tempo_medio_s"])
            iteracoes = int(linha["iteracoes"])
            memoria = float(linha["memoria_kb_media"])

            dados.setdefault(tipo, {"n": [], "tempo": [], "iteracoes": [], "memoria": []})
            dados[tipo]["n"].append(n)
            dados[tipo]["tempo"].append(tempo)
            dados[tipo]["iteracoes"].append(iteracoes)
            dados[tipo]["memoria"].append(memoria)
    return dados


def grafico_tempo_vs_n(dados):
    plt.figure(figsize=(9, 6))
    for tipo, serie in dados.items():
        plt.plot(serie["n"], serie["tempo"], marker="o", label=tipo)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Tamanho da entrada (n) - escala log")
    plt.ylabel("Tempo medio de execucao (s) - escala log")
    plt.title("Radix Sort: Tempo de execucao vs Tamanho da entrada")
    plt.legend(fontsize=8)
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    caminho = os.path.join(PASTA_SAIDA, "tempo_vs_n.png")
    plt.savefig(caminho, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Salvo: {caminho}")


def grafico_iteracoes_vs_n(dados):
    plt.figure(figsize=(9, 6))
    for tipo, serie in dados.items():
        plt.plot(serie["n"], serie["iteracoes"], marker="s", label=tipo)
    plt.xscale("log")
    plt.xlabel("Tamanho da entrada (n) - escala log")
    plt.ylabel("Numero de iteracoes (passagens por digito)")
    plt.title("Radix Sort: Iteracoes (passagens de digito) vs Tamanho da entrada")
    plt.legend(fontsize=8)
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    caminho = os.path.join(PASTA_SAIDA, "iteracoes_vs_n.png")
    plt.savefig(caminho, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Salvo: {caminho}")


def grafico_memoria_vs_n(dados):
    plt.figure(figsize=(9, 6))
    for tipo, serie in dados.items():
        plt.plot(serie["n"], serie["memoria"], marker="^", label=tipo)
    plt.xscale("log")
    plt.xlabel("Tamanho da entrada (n) - escala log")
    plt.ylabel("Memoria de pico (KB)")
    plt.title("Radix Sort: Uso de memoria vs Tamanho da entrada")
    plt.legend(fontsize=8)
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    caminho = os.path.join(PASTA_SAIDA, "memoria_vs_n.png")
    plt.savefig(caminho, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Salvo: {caminho}")


if __name__ == "__main__":
    dados = carregar_resultados()
    grafico_tempo_vs_n(dados)
    grafico_iteracoes_vs_n(dados)
    grafico_memoria_vs_n(dados)
