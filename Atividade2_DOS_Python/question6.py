# 6.Faça um Programa que leia três números e mostre o maior deles.

valor1 = int(input("\nInforme o primeiro numero: "))
valor2 = int(input("Informe o segundo numero: "))
valor3 = int(input("Informe o terceiro numero: "))

# Verificar o maior numero
print("\n")

if(valor1 > valor2 and valor1 > valor3):
    print(f"O maior numero é {valor1}")
else:
    if(valor2 > valor1 and valor2 > valor3):
        print(f"O maior numero é {valor2}")
    else:
        if(valor3 > valor1 and valor3 > valor2):
            print(f"O maior numero é {valor3}")
        else:
            print("Os valores informado são identicos")