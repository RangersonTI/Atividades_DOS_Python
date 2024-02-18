# 2.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome_usuario = None
senha = None
senha_valida = False

while not(senha_valida):
    nome_usuario = input("\n Informe o seu nome de usuário: ")
    senha = input("\n Informe uma senha: ")
    
    if(senha.upper() == nome_usuario.upper()):
        print(" ERROR... A senha informada é inválida (Senha e nome de usuário iguais)")
    else:
        senha_valida = True