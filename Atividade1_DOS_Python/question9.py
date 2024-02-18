# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

print("Fahrenheit -> Ceusius")
temp_fahrenheit = float(input("\n Informe a temperatura em Fhrenheit: "))
temp_Celsius = 5 * ((temp_fahrenheit - 32) / 9)

print(f"\nA temperatura em Celsius é de {temp_Celsius:.2f} ºC")