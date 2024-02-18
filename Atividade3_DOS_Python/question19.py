# 19.Altere o programa anterior para que ele aceite apenas números entre 0 e 1000

continuar = "S"
numeros = list()

while continuar.upper() == "S":
    numero = (int(input(" Informe um valor inteiro: ")))
    
    if(numero <0 or numero >1000):
        print("Numero informado menor que 0 e maior que 1000")
    else:
        numeros.append(numero)
    
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