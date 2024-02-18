# 17.Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

print("\n********** Ano bissexto ou não? **********\n")
ano = input("Informe um ano: ")

# Verificar tamanho da variavel ANO
tam_var_ano = len(ano)

dois_casa_decimal_de_ano = str(ano[tam_var_ano-2]) + str(ano[tam_var_ano-1])

if(dois_casa_decimal_de_ano == "00"):
    ano_bissexto = True
else:
    if(int(ano)%4 == 0):
        ano_bissexto = True
    else:
        ano_bissexto = False
        
if(ano_bissexto):
    print(f"\n{ano} é um ano bissexto\n")
else:
    print(f"\n{ano} não é um ano bissexto\n")