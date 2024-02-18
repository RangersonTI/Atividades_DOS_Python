# 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:  até 20 litros, desconto de 3% por litro   /    acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro   /    acima de 20 litros, desconto de 6% por litro 
# 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor 
# a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

def CalcularGastoCombustivel(tipo_combus,qtd_vendido):
    
    total_desconto = 0
    if(qtd_vendido <= 20 and tipo_combus.upper() == "A"):
        valor_a_pagar = (qtd_vendido*valorGasolina) + (qtd_vendido*valorAlcool)*3/100
        total_desconto = 3
    else:
        if(qtd_vendido > 20 and tipo_combus.upper() == "A"):
            valor_a_pagar = (qtd_vendido*valorGasolina) + (qtd_vendido*valorAlcool)*5/100
            total_desconto = 5
        else:
            if(qtd_vendido <= 20 and tipo_combus.upper() == "G"):
                valor_a_pagar = (qtd_vendido*valorGasolina) + (qtd_vendido*valorGasolina)*3/100
                total_desconto = 3
            else:
                if(qtd_vendido > 20 and tipo_combus.upper() == "G"):
                    valor_a_pagar = (qtd_vendido*valorGasolina) + (qtd_vendido*valorGasolina)*5/100
                    total_desconto = 5
                else:
                    print("Tipo de combustível inválido")
                    valor_a_pagar = 0
                
    return valor_a_pagar,total_desconto

valorAlcool = 1.90
valorGasolina = 2.50
    
tipo_comustivel = input("\n Informe o tipo de combustível: A - Alcool / G - Gasolina  ")
qtd_combustivel_utilizado = float(input(" Informe qtd litros gasto: "))

valor_gasto,desconto = CalcularGastoCombustivel(tipo_comustivel,qtd_combustivel_utilizado)

print(f"\n Total de litros: {qtd_combustivel_utilizado:.2f} L")
if(tipo_comustivel.upper()=="A"):
    print(" Combustível inserido: Alcool") 
else:
    if(tipo_comustivel.upper()=="G"):
        print(" Combustível inserido: Gasolina")

print(f" Total de desconto: {desconto}%")
print(f" Valor a pagar: {valor_gasto:.2f}")
