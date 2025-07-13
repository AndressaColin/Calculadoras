import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url).json()
    
    chave = moeda.upper() + "BRL"
    
    if chave in resposta:
        dados = resposta[chave]
        print(f"Moeda: {dados['name']}")
        print(f"Valor atual: R$ {dados['bid']}")
        print(f"Valor máximo: R$ {dados['high']}")
        print(f"Valor mínimo: R$ {dados['low']}")
        print(f"Última atualização: {dados['create_date']}")
    else:
        print("Moeda não encontrada ou código inválido.")

# Exemplo de uso:
moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
consultar_cotacao(moeda)
