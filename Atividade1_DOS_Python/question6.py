# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

def calcularAreaCirculo(raio):
    area = 3.14*(raio**2)
    return area

print("Calcular area do raio")
valor_raio = float(input("\n Informe o valor do raio: "))

area_circulo = calcularAreaCirculo(valor_raio)

print(f"\n A área do circulo é de {area_circulo}\n")