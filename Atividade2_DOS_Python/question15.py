# 15.Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, 
# se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

def VerificarTipoTriagunlo(lado1,lado2,lado3):
    
    idtipo_triangulo = None
    
    # A variavel vtipo_triangulo irá passar o ID de localização do tipo do triagulo atribuido na lista 'tipo_triangulo'
    if(lado1 == lado2 and lado2 == lado3):
        idtipo_triangulo = 0
    else:
        if((lado1 == lado2 and lado2 != lado3) or (lado1 == lado3 and lado1 != lado2) or lado2 == lado3 and lado1 != lado3):
            idtipo_triangulo = 1
        else:
            idtipo_triangulo = 2

    return idtipo_triangulo

tipo_triagulo = ["Equilátero","Isósceles","Escaleno"]
    
lado1 = int(input("\n Informe o tamanho do Lado1 do triângulo: "))
lado2 = int(input("\n Informe o tamanho do Lado2 do triângulo: "))
lado3 = int(input("\n Informe o tamanho do Lado3 do triângulo: "))

idtipo_triagulo = int(VerificarTipoTriagunlo(lado1,lado2,lado3))
print(f"\n Tipo do triagulo informado é: Triângulo {tipo_triagulo[idtipo_triagulo]}\n")