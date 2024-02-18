# 2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = float(input("Informe um numero qualquer: "))
print("\n")
 
if(num > 0):
    print("O numero informado é positivo")
else:
    if(num < 0):
        print("O numero informado é negativo")
    else:
        print("O numero informado é nulo")