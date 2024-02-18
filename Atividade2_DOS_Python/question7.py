# 7.Faça um Programa que leia três números e mostre o maior e o menor deles.

def verificarMaiorMenorNumero(valor1,valor2,valor3):
    
    #if(valor1 > valor2):
    
    if(valor1 == valor2 and valor2 ==valor3):
        return [None,None]
    else:    
        if(valor1 >= valor2 and valor1 >= valor3):
            if (valor2 < valor3):
                return [valor1, valor2]
            else:
                return [valor1, valor3]
        else:
            if(valor2 >= valor1 and valor2 >= valor3):
                if (valor1 < valor3):
                    return [valor2, valor1]
                else:
                    return [valor2, valor3]
            else:
                if(valor3 >= valor1 and valor3 >= valor2):
                    if (valor1 < valor2):
                        return [valor3, valor1]
                    else:
                        return [valor3, valor2]
                else:
                    return [None,None]

valor1 = int(input("\nInforme o primeiro numero: "))
valor2 = int(input("Informe o segundo numero: "))
valor3 = int(input("Informe o terceiro numero: "))

NumMaiorEMenor = verificarMaiorMenorNumero(valor1,valor2,valor3)

if(NumMaiorEMenor[0] == None):
    print("Valores informados identicos")
else:
    print(f"\n Maior valor informado: {NumMaiorEMenor[0]}")
    print(f"\n Menor valor informado: {NumMaiorEMenor[1]}")