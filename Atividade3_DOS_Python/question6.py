# 6.Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

tamanho = 20

print("\nValores um abaixo do outro")
for i in range(tamanho):
    print(i+1)
    

print("\nValores lado a lado")
for i in range(tamanho):
    if(i != tamanho-1):
        print(i+1, end=", ")
    else:
        print(i+1)