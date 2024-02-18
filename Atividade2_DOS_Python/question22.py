# 22.Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

valor = int(input("\n Informe um numero qualquer: "))

if(valor%2 == 0):
    print("\nO numero informado é par")
else:
    print("\nO numero informado é impar")