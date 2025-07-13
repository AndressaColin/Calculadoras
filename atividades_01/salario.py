numero_funcionario = int(input("Número do funcionário: "))
horas_trabalhadas = int(input("Horas trabalhadas: "))
valor_por_hora = float(input("Valor por hora: "))

salario = horas_trabalhadas * valor_por_hora

print(f"Número = {numero_funcionario}  Salário = R$ {salario:.2f}")
