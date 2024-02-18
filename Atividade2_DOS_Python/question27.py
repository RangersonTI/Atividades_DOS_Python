# 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg             Acima de 5 Kg
#   Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#   Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#   Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def ValorAPagar(kg_morango, kg_maca):
    preco_morango = 0
    preco_maca = 0

    # Calcula o preço dos morangos
    if (kg_morango <= 5):
        preco_morango = kg_morango * 2.50
    else:
        preco_morango = kg_morango * 2.20

    # Calcula o preço das maçãs
    if (kg_maca <= 5):
        preco_maca = kg_maca * 1.80
    else:
        preco_maca = kg_maca * 1.50

    # Calcula o valor total sem desconto
    valor_total_sem_desconto = preco_morango + preco_maca

    # Aplica o desconto, se aplicável
    if (kg_morango + kg_maca > 8 or valor_total_sem_desconto > 25):
        desconto = 0.10 * valor_total_sem_desconto
        valor_total_com_desconto = valor_total_sem_desconto - desconto
    else:
        valor_total_com_desconto = valor_total_sem_desconto

    return valor_total_com_desconto


kg_morango = float(input("Quantidade (em Kg) de morangos adquiridos: "))
kg_maca = float(input("Quantidade (em Kg) de maçãs adquiridas: "))


valor_a_pagar = ValorAPagar(kg_morango, kg_maca)
print(f"\nValor a ser pago pelo cliente é R$ {valor_a_pagar:.2f}")
