# 1.Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = -1
nota_valida = False

while not(nota_valida):
    nota = float(input("\n Informe uma nota de 0 à 10: "))
    if (nota>=0 and nota<=10):
        nota_valida = True
    else:
        print("Nota inválida")