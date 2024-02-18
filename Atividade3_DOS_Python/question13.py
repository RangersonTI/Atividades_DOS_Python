# 13.Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.

numero_base = int(input("\n Informe o numero base: "))
numero_expoente = int(input("\n Informe o expoente: "))

numero_potenciado = numero_base

for i in range(1,numero_expoente):
    numero_potenciado *= numero_base
    print(numero_potenciado)
    
print(f" {numero_base} elevado a {numero_expoente} é {numero_potenciado}")