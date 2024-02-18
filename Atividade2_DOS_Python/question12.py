# 12.Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto
# (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#   Desconto do IR:
#   Salário Bruto até 900 (inclusive) - isento
#   Salário Bruto até 1500 (inclusive) - desconto de 5%
#   Salário Bruto até 2500 (inclusive) - desconto de 10%
#   Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
#   No exemplo o valor da hora é 5 e a quantidade de hora é 220

def CalcularImpostos(horas_trabalhadas,valor_hora):
    
    valor_salario_buto = horas_trabalhadas*valor_hora
    valor_fgts = valor_salario_buto*11/100
    valor_IR = None
    valor_desconto_IR = None
    
    #Calcular IR
    if(valor_salario_buto <= 900):
        valor_IR = 0
        valor_desconto_IR = 0
    else:
        if(valor_salario_buto > 900 and valor_salario_buto<=1500):
            valor_IR = valor_salario_buto*5/100
            valor_desconto_IR = 5
        else:
            if(valor_salario_buto > 1500 and valor_salario_buto<=2500):
                valor_IR = valor_salario_buto*10/100
                valor_desconto_IR = 10
            else:   
                if(valor_salario_buto > 2500):
                    valor_IR = valor_salario_buto*25/100
                    valor_desconto_IR = 20

    # Vaalores passados na lista abaixo na seguinte ordem: Salario Bruto, Valor FGTS, Valor IR, Valor de desconto IR
    valores_desconto = [valor_salario_buto,valor_fgts,valor_IR,valor_desconto_IR]
    return valores_desconto

horas_trabalhadas = int(input("\n Informe o total de horas trabalhadas: "))
valor_hora = float(input(" Informe o valor da hora: "))

valores = CalcularImpostos(horas_trabalhadas, valor_hora)

# Atribuicao dos valores da lista em sua respectivas variável
#salario_bruto = valores[0], fgts_valor = valores[1], ir_valor = valores[2], valor_desc_ir = valores[3]
salario_bruto, fgts_valor, ir_valor, valor_desc_ir = valores

valor_inss = salario_bruto*10/100
total_desconto = valor_inss+ir_valor
salario_liquido = salario_bruto - total_desconto

print(f"\n Salario Bruto: R$ {salario_bruto}")
print(f" ( - ) IR ({valor_desc_ir}%): R$ {ir_valor}")
print(f" ( - ) INSS (10%): R$ {valor_inss}")
print(f" FGTS (11%): R$ {fgts_valor}")
print(f" Total descontos: R$ {total_desconto}")
print(f" Salario Líquido: R$ {salario_liquido}")