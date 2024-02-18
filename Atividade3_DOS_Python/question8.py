# 8.Faça um programa que leia 5 números e informe a soma e a média dos números.

listNumeros = list()

for i in range(5):
    listNumeros.append(int(input(f"Informe o {i+1}* numero: ")))

soma_nums = 0
media_nums = 0

for i in listNumeros:
    soma_nums += i
    
media_nums = soma_nums/len(listNumeros)     
   
print(f"\n Soma dos numeors: {soma_nums}")
print(f" Media dos numeros: {media_nums}")