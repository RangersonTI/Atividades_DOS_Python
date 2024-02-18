# Faça um Programa que peça dois números e imprima a soma.

def soma(numero1, numero2):
    resultadoSoma = numero1+numero2
    print(f"\nA soma de {numero1} e {numero2} é {resultadoSoma}\n")

print("Calculadora Soma")
num1 = float(input("\nInforme o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

soma(num1, num2)