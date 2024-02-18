# 11.Altere o programa anterior para mostrar no final a soma dos números.numero = list()
numero = list()

# Captura do valores
numero.append(int(input("\n Informe o numero inicial: ")))
numero.append(int(input(" Informe o numero final: ")))

# Ordenação dos valores (verica o menor e maior valor)

num_inicial = min(numero)
num_final = max(numero)
# Limpar lista 'numero' para reaproveitamento
numero.clear()

for i in range(num_inicial, num_final+1):
    numero.append(i)

print(f"\n Os numeros entre {num_inicial} e {num_final} são: {numero}")
print(f" A soma dos numeros é: {sum(numero)}\n")