# 9.Faça um Programa que leia três números e mostre-os em ordem decrescente.
numeros = list()
numeros.append(int(input("\n Informe o primeiro numero: ")))
numeros.append(int(input(" Informe o segundo numero: ")))
numeros.append(int(input(" Informe o terceiro numero: ")))

numeros.sort(reverse=True)

print(f"\n Valores em forma invertida: {numeros}")