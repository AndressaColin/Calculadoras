nome = input("Nome do vendedor: ")
salario_fixo = float(input("Salário fixo: "))
total_vendas = float(input("Total de vendas no mês: "))
total_receber = salario_fixo + (total_vendas * 0.15)

print(f"TOTAL = R$ {total_receber:.2f}")
