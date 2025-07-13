def verificar_palindromo(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Exemplo de uso:
frase = input("Digite uma palavra ou frase: ")
print(verificar_palindromo(frase))
