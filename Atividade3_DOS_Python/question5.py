# 5.Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

habitante_paisA = int(input("\nInforme a população do Pais A: "))
porcent_crescimento_paisA = float(input("Informe a porcentagem de crescimento do Pais A: "))
habitante_paisB = int(input("\nInforme a população do Pais B: "))
porcent_crescimento_paisB = float(input("Informe a porcentagem de crescimento do Pais B: "))
paisA_igual_paisB = False
contagem_cresc_anual = 0

#print("                       Pais A                  Pais B")
while not(paisA_igual_paisB):
    
    if(habitante_paisA < habitante_paisB):
                
        habitante_paisA = habitante_paisA + (habitante_paisA*porcent_crescimento_paisA/100)
        habitante_paisB = habitante_paisB + (habitante_paisB*porcent_crescimento_paisB/100)
        contagem_cresc_anual +=1
    else:
        paisA_igual_paisB = True
    
    #print(f" Ano {contagem_cresc_anual}: {habitante_paisA:.2f} - {habitante_paisB:.2f}")
    
    
    
print(f"\n Para que o pais A ultrapassar/igual a população com pais B demorará aproximadamente {contagem_cresc_anual} anos")