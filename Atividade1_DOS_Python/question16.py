# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

print("********** Calculo para quantidade  de tinta a utilizar **********")
area_metros_quad = float(input("\n Informe o tamanho do local (em metro quadrado quad): "))

metros_por_litro = 3
litros_p_lata = 18
valor_lata_tinta_18 = 80.00

# Variavel para calcular a quantidade de tinta total prevista na utilização da pintura
quantidade_tinta_utilizar = area_metros_quad/metros_por_litro

#Variavel para medir quantas latas são necessárias para comprar
qtd_lata_neccessarias = quantidade_tinta_utilizar//litros_p_lata

if(quantidade_tinta_utilizar%litros_p_lata!=0):
    qtd_lata_neccessarias+=1
    
valor_a_pagar = qtd_lata_neccessarias*valor_lata_tinta_18
print(f"\nSerão necessários {qtd_lata_neccessarias:.0f} latas de tinta para pinta {area_metros_quad:.2f} m2. \nValor total: R$ {valor_a_pagar:.2f}")