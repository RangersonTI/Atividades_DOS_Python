# 18.Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

continuar = "S"
numeros = list()

while continuar.upper() == "S":
    numeros.append(int(input(" Informe um valor inteiro: ")))
    continuar = input("DESEJA CONTINUAR? s -> sim / qualquer tecla - não")
    
# Fazer verificação do maior e menor numero
num_menor = numeros[0]
num_maior = numeros[0]

for cont in numeros:
    if(cont > num_maior):
        num_maior = cont
        
    if(cont < num_menor):
        num_menor = cont
        
soma_valores = sum(numeros)

print(f"\nQuantidades de valores informados: {len(numeros)}")
print(f"Maior valor: {num_maior}")
print(f"Menor valor: {num_menor}")
print(f"Soma dos valores: {soma_valores}")