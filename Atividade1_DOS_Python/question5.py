# Faça um Programa que converta metros para centímetros.

def Metro_para_centimetro(valor_metro):
    centimetro = (valor_metro*100)
    return centimetro

print("Conversor Metros -> Centimetro")

valorMetro = float(input("\n Informe o valor em metros: "))

valor_em_Cm = Metro_para_centimetro(valorMetro)
print(f"\n{valorMetro} metro equivale a {valor_em_Cm} centrimetros")