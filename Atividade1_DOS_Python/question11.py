#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) O produto do dobro do primeiro com metade do segundo. 
# b) A soma do triplo do primeiro com o terceiro.
# c) O terceiro elevado ao cubo.

def CalcularValores(inteiro1, inteiro2, num_real):
    valores = list()
    #produto do dobro do primeiro com metade do segundo.
    valor = inteiro1*2 + inteiro2/2
    valores.append(valor)
    valor = 0
    
    #soma do triplo do primeiro com o terceiro.
    valor = inteiro1*3 + num_real
    valores.append(valor)
    valor = 0
    
    #terceiro elevado ao cubo.
    valor = num_real**3
    valores.append(valor)
    valor = 0
    
    return valores
    
num_int_1 = int(input("Informe o primero numero inteiro: "))
num_int_2 = int(input("Informe o segundo numero inteiro: "))
num_float = float(input("Informe um numero real: "))

valores = CalcularValores(num_int_1,num_int_2,num_float)
print(f"\n O produto do dobro do primeiro com metade do segundo é: {valores[0]}")
print(f" A soma do triplo do primeiro com o terceiro é: {valores[1]}")
print(f" O terceiro elevado ao cubo: {valores[2]}")