# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
divisiveis_por_Numero = list()
numero = int(input("Informe um numero: "))


for i in range(1,numero+1):
    if(numero%i==0):
        divisiveis_por_Numero.append(i)

if(len(divisiveis_por_Numero)==2):
    print(f"Numero primo: {divisiveis_por_Numero}")
else:
    print(f"Numero não primo: {divisiveis_por_Numero}")