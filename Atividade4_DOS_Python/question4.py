# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor = ['c','r','t','u','i','v','m','a','e','p']
contConsoante = 0
for i in range(len(vetor)):
    vetor[i] = vetor[i].upper()
    
for i in range(len(vetor)):
    if(vetor[i] not in ('A','E','I','O','U')):
        contConsoante+= 1
        
print(f"A quantidade de consoantes no vetor e {contConsoante}")