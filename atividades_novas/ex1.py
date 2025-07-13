while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Escolha a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida. Use +, -, *, /.")

        print(f"Resultado: {resultado}")
        break

    except ValueError as e:
        print(f"Erro: {e}. Tente novamente.")
    except ZeroDivisionError as e:
        print(f"Erro: {e}. Tente novamente.")
