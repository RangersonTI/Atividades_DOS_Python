# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#   comprar apenas latas de 18 litros;
#   comprar apenas galões de 3,6 litros;
#   misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
# considere latas cheias.

import math

def calcular_tinta(area, rendimento):
#Adicionar 10% de folga
    area_com_folga = area * 1.1

#Arredondar para cima o número de latas
    latas = math.ceil(area_com_folga / rendimento)
    return latas

#Definir as variáveis
area = float(input("Digite a área a ser pintada (em metros quadrados): "))
rendimento_lata = 18 * 6  # 18 litros de tinta cobrem 108 metros quadrados
preco_lata = 80.00
rendimento_galao = 3.6 * 6  # 3,6 litros de tinta cobrem 21,6 metros quadrados
preco_galao = 25.00

#Calcular a quantidade de tinta em latas
latas_necessarias = calcular_tinta(area, rendimento_lata)
preco_total_latas = latas_necessarias * preco_lata

#Calcular a quantidade de tinta em galões
galoes_necessarios = calcular_tinta(area, rendimento_galao)
preco_total_galoes = galoes_necessarios * preco_galao

#Calcular a quantidade de tinta mista (latas e galões)
latas_mistas = math.floor(area / rendimento_lata)
galao_misto = math.ceil((area - latas_mistas * rendimento_lata) / rendimento_galao)
preco_total_misto = latas_mistas * preco_lata + galao_misto * preco_galao

#Mostrar os resultados
print("Compra apenas em latas:")
print(f"Quantidade de latas: {latas_necessarias}")
print(f"Preço total: R$ {preco_total_latas:.2f}")

print("\nCompra apenas em galões:")
print(f"Quantidade de galões: {galoes_necessarios}")
print(f"Preço total: R$ {preco_total_galoes:.2f}")

print("\nCompra mista (latas e galões):")
print(f"Quantidade de latas: {latas_mistas}")
print(f"Quantidade de galões: {galao_misto}")
print(f"Preço total: R$ {preco_total_misto:.2f}")