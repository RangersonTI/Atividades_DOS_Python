# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#   Os juros e a quantidade de parcelas seguem a tabela abaixo:
#       Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#       1       0
#       3       10
#       6       15
#       9       20
#       12      25
#   Exemplo de saída do programa:
#       Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#       R$ 1.000,00     0               1                       R$  1.000,00
#       R$ 1.100,00     100             3                       R$    366,00
#       R$ 1.150,00     150             6                       R$    191,67

def ValorAPagarDivida(valorDivida,divisao_parcela):

    valorTotalAPagar = 0
    porcentJuros = 0
    valorJuros = 0

    if(divisao_parcela == 1):
        porcentJuros = 0
        valorJuros = valorDivida*porcentJuros/100
        valorTotalAPagar = valorDivida + valorJuros
        return[valorTotalAPagar, valorJuros]
    else:
        if(divisao_parcela == 3):
            porcentJuros = 10
            valorJuros = valorDivida*porcentJuros/100
            valorTotalAPagar = valorDivida + valorJuros
            return[valorTotalAPagar, valorJuros]
        else:
            if(divisao_parcela == 6):
                porcentJuros = 15
                valorJuros = valorDivida*porcentJuros/100
                valorTotalAPagar = valorDivida + valorJuros
                return[valorTotalAPagar, valorJuros]
            else:
                if(divisao_parcela == 9):
                    porcentJuros = 20
                    valorJuros = valorDivida*porcentJuros/100
                    valorTotalAPagar = valorDivida + valorJuros
                    return[valorTotalAPagar, valorJuros]
                else:
                    if(divisao_parcela == 12):
                        porcentJuros = 25
                        valorJuros = valorDivida*porcentJuros/100
                        valorTotalAPagar = valorDivida + valorJuros
                        return[valorTotalAPagar, valorJuros]
                    
valor_valido = False
parcela_valida = (1,3,6,9,12)

valorDivida = float(input("\nInforme o valor da divida: "))
while not valor_valido:
    qtd_parcela = int(input("\nQuantas parcelas deseja dividir o pagamento (haverá juros): \n1 - 1 parcela\n3 - 3 parcelas\n6 - 6 parcelas\n9 - 9 parcelas\n12 - 12 parcelas\t"))
    if(qtd_parcela in parcela_valida):
        valor_valido = True
    else:
        print("Opção inválida. Selecione um opção valida")
    
total_a_pagar = ValorAPagarDivida(valorDivida,qtd_parcela)

valor_divida = total_a_pagar[0]
valor_juros = total_a_pagar[1]
print(f"\nValor da dívida: R$ {valor_divida}\nValor dos Juros: R$ {valor_juros}\nQuantidade de parcelas: {qtd_parcela}\nValor da parcela: R$ {valor_divida/qtd_parcela:.2f}")