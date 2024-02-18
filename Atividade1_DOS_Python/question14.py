# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

print("******** Calculo de multa ********")

qtd_peixes_pescado = float(input("\nInforme a quantidade peixes pescado hoje (em Kg): "))
peso_limite = int(50)
valor_multa_kg = int(4)

if (qtd_peixes_pescado>peso_limite):
    peso_ultrapassado = (qtd_peixes_pescado - peso_limite)
    valor_a_pagar = peso_ultrapassado*4
    print("\nQuantidade excedida.")
    print(f"Qtd excedida: {peso_ultrapassado:.2f} Kg")
    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
else:
    print("Peso não excedido")