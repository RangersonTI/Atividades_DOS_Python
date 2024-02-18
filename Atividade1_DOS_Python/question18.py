# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print("Calculo de tempo de Download")
tamanho_arquivo = int(input("\n Informe o tamanho do arquivo (em Mb): "))
velocidade_link = int(input(" Informe a velocidade do link (em Mbps): "))

tempo_download_seg = tamanho_arquivo/velocidade_link
tempo_download_min = tempo_download_seg//60
tempo_restante = tempo_download_seg%60

print(f"\n O tempo de download será de {tempo_download_min:.0f} min e {tempo_restante:.0f} seg\n")