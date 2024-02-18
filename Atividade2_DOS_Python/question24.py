# 24.Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#   par ou ímpar;
#   positivo ou negativo;
#   inteiro ou decimal.

def CalcularValores(nota1,nota2,op):
    
    resultado = float
    if(op == 0):
        resultado = nota1+nota2
    else:
        if(op == 1):
            resultado = nota1-nota2
        else:
            if(op == 2):
                resultado = nota1*nota2
            else:
                if(op == 3):
                    if(nota2 == 0):
                        resultado = None
                    else:
                        resultado = nota1/nota2
                else:
                    if(op == 4):
                        resultado = nota1%nota2
                    else:
                        print("Opcao inválida")
                        
    return resultado

valor1 = float(input("\n Informe o primeiro numero: "))
valor2 = float(input(" Informe o segundo numero: "))
operacao = int(input("\n Inform o tipo de operacao: \n0 - Soma\n1 - Subtracao\n2 - Multiplicacao\n3 - Divisão\n4 - Resto Divisão\t"))

resultado = CalcularValores(valor1,valor2,operacao)
par_impar = None
posi_nega = None
Int_Decimal = None

# Verificar se é par ou impar
if(resultado%2 == 0):
    par_impar = "Par"
else:
    par_impar = "Impar"

# Verificar se numero é positivo
if(resultado > 0):
    posi_nega = "Positivo"
else:
    posi_nega = "Negativo"

# Verificar se numero é inteiro ou decimal
if(resultado.is_integer()):
    Int_Decimal = "Inteiro"
else:
    Int_Decimal = "Decimal"
    
print(f"\n Resultado: {resultado}")
print(f"O resultado é um numero {posi_nega}, {par_impar} e {Int_Decimal}")