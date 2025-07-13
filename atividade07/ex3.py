import json

# Dados iniciais
pessoa = {
    "nome": "Andressa",
    "idade": 25,
    "cidade": "Corumbá"
}

# Escrevendo no arquivo
with open("pessoa.json", "w") as arquivo:
    json.dump(pessoa, arquivo, indent=4)

# Lendo do arquivo
with open("pessoa.json", "r") as arquivo:
    dados = json.load(arquivo)
    print("Dados lidos do JSON:")
    print(dados)
