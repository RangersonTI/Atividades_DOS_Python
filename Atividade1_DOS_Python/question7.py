# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def calcularAreaQuadrado(area_aresta):
    area_quadrado = area_aresta**2
    return area_quadrado

aresta_quadrado = int(input("Informe o tamanho da aresta: "))
area_quadrado_dobrado = calcularAreaQuadrado(aresta_quadrado) * 2

print(f"\nO dobro da área do quandrado é {area_quadrado_dobrado}\n")
