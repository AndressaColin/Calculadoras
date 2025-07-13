while True:
    senha = input("Digite uma senha forte (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        print("Encerrando verificação.")
        break

    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.")
        continue

    if not any(char.isdigit() for char in senha):
        print("Senha fraca: deve conter pelo menos um número.")
        continue

    print("Senha forte cadastrada com sucesso!")
    break
