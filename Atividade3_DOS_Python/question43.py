# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) 
# e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

# Lista do cardapio
cardapio = [
    {'cod':100, 'descricao': "Cachorro Quente", 'valor': 1.20},
    {'cod':101, 'descricao': "Bauru Simples", 'valor': 1.30},
    {'cod':102, 'descricao': "Bauru com ovo", 'valor': 1.50},
    {'cod':103, 'descricao': "Hambúrguer", 'valor': 1.20},
    {'cod':104, 'descricao': "Cheeseburger", 'valor': 1.30},
    {'cod':105, 'descricao': "Refrigerante", 'valor': 1.00}
]

# Funcao para obter o preco do produto pelo codigo
def ObterValor_PCod(cod):
    for i in cardapio:
        if(i['cod'] == cod):
            return i['valor']

# Funcao para obter a descricao do produto pelo codigo
def ObterDescProduto_PCod(cod):
    for d in cardapio:
        if(d['cod'] == cod):
            return d['descricao']

# Funcao para calcular o valor por item
def CalcularValor(pedido):
    calculo_pedido_total = list()
    
    for i in pedido:
        cod_produto = i['cod']
        quantidade = i['quantidade']
        valor_unitario_pedido = ObterValor_PCod(cod_produto)
        valor_total_item = valor_unitario_pedido*quantidade
        
        calculo_pedido_total.append({'cod': cod_produto, 'valor_total_item': valor_total_item, 'qtd': quantidade})
        
    MostrarValores(calculo_pedido_total)

# Funcao para mostrar os valor (Ex: NF)
def MostrarValores(valores_pedido):
    print("\n")
    for p in valores_pedido:
        cod_produto = p['cod']
        desc_produto = ObterDescProduto_PCod(cod_produto)
        valor_a_pagar = p['valor_total_item']
        qtd = p['qtd']
        
        print(f"{desc_produto}: R${valor_a_pagar:.2f}   Qtd: {qtd}")
        


fechar_pedido = False
adicionar_pedido = list()

while not(fechar_pedido):
    
    
    print("Cardapio do dia. Escolha um: (Informe o codigo do produto)")
    print("\nProduto:         Valor           Codigo")
    
    for i in cardapio:
        print(f"{i['descricao']}    {i['valor']}    {i['cod']}")
    
    prod_cod_escolha = int(input(""))
    qtd_prod = int(input("Informe a quantidade desejada: "))
    
    if any(prod_cod_escolha == item['cod'] for item in cardapio):
        adicionar_pedido.append({'cod': prod_cod_escolha, 'quantidade': qtd_prod})
        
        fechar_pedido_opc = int(input(("\nFechar pedido? 0 - Não  /  1 - Sim ")))
        if(fechar_pedido_opc == 1):
            fechar_pedido = True
        else:
            continue
    else:
        print("\nPRODUTO INVÁLIDO\n")
        
CalcularValor(adicionar_pedido)