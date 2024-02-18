# 4.Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que 
# a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos 
# necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

habitante_paisA = 80000
porcent_crescimento_paisA = 3
habitante_paisB = 200000
porcent_crescimento_paisB = 1.5
paisA_igual_paisB = False
contagem_cresc_anual = 0

#print("                       Pais A                  Pais B")
while not(paisA_igual_paisB):
    habitante_paisA = habitante_paisA + (habitante_paisA*porcent_crescimento_paisA/100)
    habitante_paisB = habitante_paisB + (habitante_paisB*porcent_crescimento_paisB/100)
    contagem_cresc_anual +=1
    
    #print(f" Ano {contagem_cresc_anual}: {habitante_paisA:.0f} - {habitante_paisB:.0f}")
    
    if(habitante_paisA >= habitante_paisB):
        paisA_igual_paisB = True
    
print(f" Para que o pais A ultrapassar/igual a população com pais B demorará aproximadamente {contagem_cresc_anual} anos")