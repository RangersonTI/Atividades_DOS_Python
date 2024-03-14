# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num 
# vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

nota1 = [6,8,5,8.5,4,6,9,8,9,10]
nota2 = [6,7,5,8,8,9,7,8.5,7,3.5]
nota3 = [5.7,7,5,8,8,9,10,8,8,7]
nota4 = [7,2,5,7,7,3,6,9,7,8]

mediaNotas = []
contarNotaMaior7 = 0

for i in range(len(nota1)):
    print(i)
    media = nota1[i]+nota2[i]+nota3[i]+nota4[i]/4
    mediaNotas.append(media)
    
for i in mediaNotas:
    if i >= 7:
        contarNotaMaior7 +=1

print(f"Quantidade de alunos com media >= 7: {contarNotaMaior7}")