# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = [3,6,3,19,7,21,9,4,2,0]

print(f"Valores do vetor: {vetor}")
print(f"Valores do vetor inverso: ",end="")

for i in range(len(vetor)-1,-1,-1):
    print(vetor[i],end=",")