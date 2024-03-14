# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num 
# vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

nota1 = list()
nota2 = list()
nota3 = list()
nota4 = list()
nota = list()

mediaNotas = []
qtdAlunos = 10
contarNotaMaior7 = 0

for i in range(qtdAlunos):
    print(f" **\n Notas do aluno {i+1} **\n")
    for i in range(4):
        nota.append(float(input(f"Informe a {i+1}* nota: ")))

    nota1.append(nota[0])
    nota2.append(nota[1])
    nota3.append(nota[2])
    nota4.append(nota[3])
    nota.clear()

for i in range(len(nota1)):
    media = (nota1[i]+nota2[i]+nota3[i]+nota4[i])/4
    mediaNotas.append(media)

print(mediaNotas+"\n")
for i in mediaNotas:
    if i >= 7:
        contarNotaMaior7 +=1

print(f"Quantidade de alunos com media >= 7: {contarNotaMaior7}")