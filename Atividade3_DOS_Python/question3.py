# 3.Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

def ValidarDados(nome,idade,salario,sexo,estado_civil):
    validado_error = False
    
    if(len(nome) <= 3):
        print(" Nome de conter mais de 3 caracteres")
        return validado_error
    
    if(idade<0 and idade<150 ):
        print(" Idade inválida. Idade deve ser entre 0 e 150 anos")
        return validado_error
    
    if(salario <0):
        print(" Salário informado menor que 0")
        return validado_error
    
    if(sexo != "M" and sexo != "F"):
        print(f" Sexo inválido. OPção informada: {sexo}")
        return validado_error
    
    if(estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d"):
        print(f" Opção inválida. Opção informada: {estado_civil}")
        return validado_error
    
    return True

validado = False

while not(validado):    
    nome = input("\n Informe o seu nome: ")
    idade = int(input(" Informe a sua idade: "))
    salario = float(input(" Informe o seu salario: "))
    sexo = input(" Informe seu sexo: F - Feminino  /  M - Masculino ").upper()
    estado_civil = input(" Informe o seu estavo civil: \nS - Soltero\nC - Casado\nV - Viuvo\nD - Divorciado:    ").lower()

    validado = ValidarDados(nome,idade,salario,sexo,estado_civil)
