# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def calcularMedia(notas):
    media = sum(notas)/4
    print(f"\nA média do aluno é {media}\n")


# lista de notas
notas = []

print("Calcular Media")
notas.append(float(input("\n Informe a 1º nota: ")))
notas.append(float(input(" Informe a 2º nota: ")))
notas.append(float(input(" Informe a 3º nota: ")))
notas.append(float(input(" Informe a 4º nota: ")))

calcularMedia(notas)