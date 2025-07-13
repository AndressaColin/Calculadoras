import statistics

tempos = []

with open("log.txt", "r") as arquivo:
    for linha in arquivo:
        if "Tempo de execução:" in linha:
            tempo = float(linha.strip().split(":")[1])
            tempos.append(tempo)

media = statistics.mean(tempos)
desvio = statistics.stdev(tempos)

print(f"Média do tempo: {media:.2f} segundos")
print(f"Desvio padrão: {desvio:.2f} segundos")

