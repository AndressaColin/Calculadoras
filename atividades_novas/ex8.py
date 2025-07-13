from datetime import datetime

def idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade * 365

# Exemplo de uso:
ano = int(input("Digite o ano de nascimento: "))
dias = idade_em_dias(ano)
print(f"Sua idade em dias (aproximadamente): {dias} dias")
