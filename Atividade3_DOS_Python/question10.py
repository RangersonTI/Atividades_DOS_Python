# 10.Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
numero = list()

# Captura do valores
numero.append(int(input("\n Informe o numero inicial: ")))
numero.append(int(input(" Informe o numero final: ")))

# Ordenação dos valores (verica o menor e maior valor)

num_inicial = min(numero)
num_final = max(numero)
numero.clear()

for i in range(num_inicial, num_final+1):
    numero.append(i)
    
print(f"\n Os numeros entre {num_inicial} e {num_final} são: {numero}")