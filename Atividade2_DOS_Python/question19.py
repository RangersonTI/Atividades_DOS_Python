# 19.Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo
# 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

def VerificarCasas(numero):

    if(numero >=1000):
        print("Numero inválido. Valor deve ser menor que 1000")
    else:
        centena = numero // 100
        dezena = (numero % 100) // 10
        unidade = numero % 10
        result = ""
        
        if(centena > 0):
            if(centena == 1):
                result += f"{centena} centena"
            else:
                result += f"{centena} centenas"
                
        if(dezena > 0):
            if(result != ""):
                if(unidade == 0):
                    result += " e "
                else:
                    result += ", "
            if(dezena == 1):
                result += f"{dezena} dezena"
            else:
                result += f"{dezena} dezenas"
        
        if(unidade > 0):
            if(centena == 0 and dezena ==0):
                result+=""
            else:
                result += " e "
                
            if(unidade == 1):
                result += f"{unidade} unidade"
            else:
                result += f"{unidade} unidades"
        
    return result

numeros = [326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 ,16]

for numero in numeros:
    print(f"{numero} = {VerificarCasas(numero)}")