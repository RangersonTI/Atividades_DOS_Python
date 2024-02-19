# 20.Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o 
# fatorial a números inteiros positivos e menores que 16.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

while True:
    try:
        numero = int(input("\nDigite um número inteiro positivo menor que 16 para calcular o fatorial (ou digite um número negativo para sair): "))
        if numero < 0:
            print("Encerrando o programa...")
            break
        elif numero >= 16:
            print("Por favor, insira um número inteiro positivo menor que 16.")
        else:
            resultado = fatorial(numero)
            print("O fatorial de", numero, "é:", resultado)
    except ValueError:
        print("Por favor, insira um número inteiro válido.")