# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

def VerificarTipoAcrescimo(salario):
    lista_Valores = list()
    if(salario <= 280):
        # reajuste de 20%
        lista_Valores = CalcularAcrescimo(salario,20)
    else:
        if(salario > 280 and salario <= 700):
        # reajuste de 15%
            lista_Valores = CalcularAcrescimo(salario,15)
        else:
            if(salario > 700 and salario <= 1500):
            # reajuste de 10%
                lista_Valores = CalcularAcrescimo(salario,10)
            else:
                if(salario >= 1500):
                # reajuste de 5%
                    lista_Valores = CalcularAcrescimo(salario,5)
                else:
                    return 0
    
    # Retornar salario reajustado, valor acrescentado e porcetagem  de aumento
    return lista_Valores
                
def CalcularAcrescimo(salario, porcent_acrescimo):
    salario_reajuste = salario + (salario*porcent_acrescimo/100)
    valor_acrescimo = salario_reajuste - salario
    return [salario_reajuste,valor_acrescimo,porcent_acrescimo]


valor_salario = float(input("Informe o seu salario: "))
informacoes_aumento = VerificarTipoAcrescimo(valor_salario)

print(f"\n Salário anterior: R$ {valor_salario:.2f}")
print(f"Percentual de aumento: {informacoes_aumento[2]}%")
print(f"Valor de aummentado: R$ {informacoes_aumento[1]:.2f}")
print(f"Novo salario: R$ {informacoes_aumento[0]:.2f}")