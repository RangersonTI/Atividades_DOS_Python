# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = C x 1,8 + 32.

print("Ceusius -> Fahrenheit")
temp_Celsius = float(input("\n Informe a temperatura em Celsius: "))
temp_Fahrenheit = temp_Celsius * 1.8 + 32

print(f"\nA temperatura em Fahrenheit é de {temp_Fahrenheit:.2f} ºF")