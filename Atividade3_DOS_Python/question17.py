# 17.Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numero = int(input("Informe um valor para calcular o fatorial: "))

# Verifica se o número é negativo
if numero < 0:
    print("O fatorial não está definido para números negativos.")
else:
    resultado = fatorial(numero)
    print(f"O fatorial de {numero} é: {resultado}")