# 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno_estudo = input("Informe o turno em você estuda: M - Matutino ou V - Vespertino ou N - Noturno  ")

if(turno_estudo == "M" or turno_estudo == "m"):
    print("Bom dia")
else:
    if(turno_estudo[0] == "V" or turno_estudo == "v"):
        print("Boa tarde")
    else:
        if(turno_estudo == "N" or turno_estudo == "n"):
            print("Boa noite")
        else:
            print("Opção inválida")