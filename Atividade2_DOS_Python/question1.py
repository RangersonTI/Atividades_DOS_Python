# 1.Faça um Programa que peça dois números e imprima o maior deles.

valor1 = int(input("\nInforme o primeiro numero: "))
valor2 = int(input("\nInforme o segundo numero: "))

# Verificar o maior numero
print("\n")
if(valor1 > valor2):
    print(f"Valor maior: {valor1}")
else:
    if(valor2 > valor1):
        print(f"Valor maior: {valor2}")
    else:
        print("Valores identicos")