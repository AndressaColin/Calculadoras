import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso:
qtd = int(input("Informe a quantidade de caracteres da senha: "))
print("Senha gerada:", gerar_senha(qtd))
