# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#   salário bruto.
#   quanto pagou ao INSS.
#   quanto pagou ao sindicato.
#   o salário líquido.
#  calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

def CalcularValoresImpostos(valor_bruto):
    imposto_renda = valor_bruto*11/100
    inss = valor_bruto*8/100
    sindicato = valor_bruto*5/100
    salario_liquido = valor_bruto - (imposto_renda + inss + sindicato)
    
    print(f" Imposto de Renda: {imposto_renda}")
    print(f" INSS: {inss}")
    print(f" Sindicato: {sindicato}")
    print(f" Salario Liquido: {salario_liquido}")

print("******* Calculando impostos a pagar *******")
valor_ganho_horario = float(input("\n Informe seu valor ganho por hora: "))
horas_trabalhadas_mes = int(input("Informe a quantidade de horas trabalhadas por mês: "))

valor_bruto = valor_ganho_horario*horas_trabalhadas_mes
print(f"\n Salario Bruto: {valor_bruto}")
valores = CalcularValoresImpostos(valor_bruto)