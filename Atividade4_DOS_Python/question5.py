# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

vetorPrincipal = list()
vetorPar = list()
vetorImpar = list()

for i in range(20):
    vetorPrincipal.append(int(input(f"Inforome o valor da posicao {i+1}: ")))
    
for i in range(len(vetorPrincipal)):
    if(vetorPrincipal[i]%2 == 0):
        vetorPar.append(vetorPrincipal[i])
    else:
        vetorImpar.append(vetorPrincipal[i])
        
print(f"Vetor principal: {vetorPrincipal}")
print(f"Vetor com valores pares: {vetorPar}")
print(f"Vetor com valores impares: {vetorImpar}")