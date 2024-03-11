# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = list()
print("Calculo de notas: \n")

for i in range(4):
    notas.append(float(input(f"Informe a {i+1}* nota: ")))

print("\n")
media = sum(notas)/len(notas)

for i in range(len(notas)):
    print(f"Nota {i+1}: {notas[i]}")
print(f"A media do aluno e: {media}")