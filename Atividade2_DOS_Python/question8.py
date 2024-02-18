# 8.Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

nome_produto = list()
preco_produto = list()

for i in range(3): 
    nome_produto.append(input(f"\n Informe o nome do produto numero {i+1}: ")) 
    preco_produto.append(float(input(" Informe o valor deste produto: ")))

produto_mais_barato = preco_produto.index(min(preco_produto))

print(f"\n Produto mais em conta: {nome_produto[produto_mais_barato]} -> {preco_produto[produto_mais_barato]}")