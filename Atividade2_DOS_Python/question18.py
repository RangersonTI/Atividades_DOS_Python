# 18.Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

def ValidarData(data):
    dia, mes, ano = map(int, data.split("/"))

    if ano > 0:
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= dia <= 31
        elif mes in [4, 6, 9, 11]:
            return 1 <= dia <= 30
        elif mes == 2:
            if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
                return 1 <= dia <= 29
            else:
                return 1 <= dia <= 28
    return False
    
data = input("\nInforme uma data (no formato dd/mm/aaaa): ")

data_valida = ValidarData(data)
if data_valida:
    print("\nA data informada é válida")
else:
    print("\nA data informada é inválida")
