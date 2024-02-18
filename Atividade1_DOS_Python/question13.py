# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

print("Calculando peso ideal (H / M)")
altura = float(input("\n Informe a sua altura: "))
sexo = input("\n Informe: H para homem  /  M para mulher ")

if (sexo == "H" or sexo == "h"):
    peso_homem =  (72.7 * altura) - 58
    print(f"\nSeu peso ideal seria de {peso_homem:.2f} kg")
else:
    if (sexo == "M" or sexo == "m"):
        peso_homem =  (62.1 * altura) - 44.7
        print(f"\nSeu peso ideal seria de {peso_homem:.2f} kg")
    else:
        print("A opção informa não é válida")