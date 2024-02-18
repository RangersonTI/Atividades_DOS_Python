# 7.Faça um programa que leia 5 números e informe o maior número.

listNumeros = list()

for i in range(5):
    listNumeros.append(int(input(f"Informe o {i+1}* numero: ")))

num = listNumeros[0]

for i in listNumeros:
    if(i > num):
        num = i
        
print(f" Maior número inserido: {num}")