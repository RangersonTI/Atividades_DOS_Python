# 25.Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

print(" ************* Investigacao iniciada... ************* \n")
print(" Responda as seguites perguntas\n")
pergunta1 = input("Telefonou para a vítima?  1 - Sim  /  0 - Não ")
pergunta2 = input("Esteve no local do crime? 1 - Sim  /  0 - Não ")
pergunta3 = input("Mora perto da vítima? 1 - Sim  /  0 - Não ")
pergunta4 = input("Devia para a vítima? 1 - Sim  /  0 - Não ")
pergunta5 = input("Já trabalhou com a vítima? 1 - Sim  /  0 - Não ")
print("\n")

perguntas = [pergunta1,pergunta2,pergunta3,pergunta4,pergunta5]
resposta_positiva = 0

for pergunta in range (len(perguntas)):
    if(perguntas[pergunta] == "1"):
        resposta_positiva += 1
        
if(resposta_positiva == 0 or resposta_positiva == 1):
    print(" Pessoa considerada inocente")
else:
    if(resposta_positiva == 2):
        print(" Pessoa considerada suspeita")
    else:
        if(resposta_positiva == 3 or resposta_positiva == 4):
            print(" Pessoa considerada cumplice")
        else:
            print(" Pessoa considerada assassina")