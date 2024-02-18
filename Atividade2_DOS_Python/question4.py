# 4.Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("\nInforme uma letra qualquer: ")
letra = letra.upper()

if (letra[0] == "A" or letra[0] == "E" or letra[0] == "I" or letra[0] == "O" or letra[0] == "U"):
    print("\n A letra informada é uma vogal")
else:
    print("\n A letra informada é uma consoante")