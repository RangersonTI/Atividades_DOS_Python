# 12.Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
print("************ Tabuada ************")

casa_tabuada = int(input(" Informe a casa desejada: "))

for i in range(10):
    print(f" {casa_tabuada} X {i+1} = {casa_tabuada*(i+1)}")