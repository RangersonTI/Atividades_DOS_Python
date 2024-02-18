# 28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg             Acima de 5 Kg
#  File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#  Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#  Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#  Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne
# comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


precos = {
    "File Duplo": {"ate_5kg": 4.90, "acima_de_5kg": 5.80},
    "Alcatra": {"ate_5kg": 5.90, "acima_de_5kg": 6.80},
    "Picanha": {"ate_5kg": 6.90, "acima_de_5kg": 7.80}
}


tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ").strip().title()
quantidade = float(input("Digite a quantidade em Kg: "))

# Verificando o preço com base na quantidade
if (quantidade <= 5):
    preco_total = quantidade * precos[tipo_carne]["ate_5kg"]
else:
    preco_total = quantidade * precos[tipo_carne]["acima_de_5kg"]

# Solicitando o tipo de pagamento e calculando o desconto
tipo_pagamento = input("Digite o tipo de pagamento (0 - Cartao Tabajara ou 1 - Outro): ").strip().title()
if (tipo_pagamento == "0"):
    desconto = 0.05 * preco_total
    nome_tipo_pagamento = "Cartão Tabajara"
else:
    desconto = 0
    nome_tipo_pagamento = "Outros"

# Calculando o valor a ser pago
valor_pagar = preco_total - desconto

# Imprimindo o cupom fiscal
print("\n=== Cupom Fiscal ===")
print(f"Tipo de carne {tipo_carne}")
print(f"Quantidade: {quantidade }Kg")
print(f"Preço total: R$ {preco_total}")
print(f"Tipo de pagamento {nome_tipo_pagamento}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_pagar:.2f}")
