# 14.Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E

def CalcularMedia(nota1, nota2):
    media = (nota1+nota2)/2
    return media
    
nota1 = float(input("Informe a primiera nota: "))
nota2 = float(input("Informe a segunda nota: "))

nota_media = CalcularMedia(nota1,nota2)
nota_conceito = None

if(nota_media >= 9):
    nota_conceito = "A"
else:
    if(nota_media >= 7.5 and nota_media < 9):
        nota_conceito = "B"
    else:
        if(nota_media >= 6 and nota_media < 7.5):
            nota_conceito = "C"
        else:
            if(nota_media >= 4 and nota_media < 6):
                nota_conceito = "D"
            else:
                if(nota_media >=0 and nota_media < 4):
                    nota_conceito = "E"
                else:
                    nota_conceito = None
                    
print(f"\n Nota do aluno: {nota_media}")
print(f" Conceito: {nota_conceito}")
if(nota_conceito == "A" or nota_conceito == "B" or nota_conceito == "C"):
    print(" APROVADO")
else:
    print(" REPROVADO")
