# 3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = (input("\nInforme uma letra: "))

if letra.upper() == "F":
    print("F - Feminino")
else:
    if letra.upper() == "M":
        print("M - Masculino")
    else:
        print("Sexo inválido")