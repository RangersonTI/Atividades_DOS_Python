# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

print("Calculando ganho mensal")

valor_p_hora = float(input("\n Informe o valor ganho em 1 hora: "))
horas_trabalhadas = int(input("\n Informe quantidade de horas trabalhadas: "))

total_ganho = valor_p_hora * horas_trabalhadas

print(f"\nSeu salario no mês foi de R$ {total_ganho}\n")