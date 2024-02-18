# 14.Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

numeros = list()
tamanho = 10
qtdNumImpar = 0
qtdNumPar = 0

for i in range(tamanho):
    numeros.append(int(input(f" Informe o {i+1}* numero: ")))
    
for i in numeros:
    if(i%2 == 0):
        qtdNumPar+=1
    else:
        qtdNumImpar+=1
        
print(f"\nNumeros informados: {numeros}")
print(f"Numeros pares: {qtdNumPar}\nNumeros impares: {qtdNumImpar}")