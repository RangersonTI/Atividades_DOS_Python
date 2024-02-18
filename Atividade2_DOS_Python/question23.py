# 23.Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero = float(input("Informe um numero: "))

if(numero.is_integer()):
    print("\n O numero informado é do tipo Inteiro")
else:
    print("\n O numero informado é do tipo Decimal")