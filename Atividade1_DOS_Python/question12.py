# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

def CalculandoPesoAproxmado(altura):
    peso_aproximado = (72.2*altura) - 58
    print(f"\nO peso ieal para uma pessoa de {altura} é {peso_aproximado:.2f} kg")

print("******** Procurando o peso aproximado ********")
altura = float(input("\n Informe a sua altura: "))
CalculandoPesoAproxmado(altura)