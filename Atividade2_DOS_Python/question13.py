# 13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

def VerificarDiaSemana(numero):
    
    DiasSemana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]
    
    if(numero == 1):
        return DiasSemana[0]
    else:
        if(numero == 2):
            return DiasSemana[1]
        else:
            if(numero == 3):
                return DiasSemana[2]
            else:
                if(numero == 4):
                    return DiasSemana[3]
                else:
                    if(numero == 5):
                        return DiasSemana[4]
                    else:
                        if(numero == 6):
                            return DiasSemana[5]
                        else:
                            if(numero == 7):
                                return DiasSemana[6]
                            else:
                                return 0
    
numero = int(input("Informe um numero de 1 à 7: "))

diaSemana = VerificarDiaSemana(numero)

if(diaSemana == 0):
    print("Numero inválido. Valor não condiz com um dia da semana")
else:
    print(diaSemana)