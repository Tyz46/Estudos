'''Implemente um programa que leia o destino do passageiro, se a viagem inclui retorno
(ida e volta) e informar o preço da passagem conforme a tabela a seguir.'''

viagem = input("Para onde deseja viajar? Opções: Região Norte, Região Nordeste, Região Centro-Oeste e Região Sul. ")
ida_vlt = input("Deseja ida e volta? (Sim ou Não)")

rn = 500
rndst = 350
rco = 350
rs = 300

if viagem == "Região Norte":
    if ida_vlt == "Sim":
        rn = rn + 400
        print("Valor total a pagar de ida e volta:", rn)
    else:
        print("Valor total a pagar só de ida:", rn)
elif viagem == "Região Nordeste":
    if ida_vlt == "Sim":
        rndst = rndst + 300
        print("Valor total a pagar de ida e volta:", rndst)
    else:
        print("Valor total a pagar só de ida:", rndst)
elif viagem == "Região Centro-Oeste":
    if ida_vlt == "Sim":
        rco = rco + 250
        print("Valor total a pagar de ida e volta:", rco)
    else:
        print("Valor total a pagar só de ida:", rco)
elif viagem == "Região Sul":
    if ida_vlt == "Sim":
        rs = rs + 250
        print("Valor total a pagar de ida e volta:", rs)
    else:
        print("Valor total a pagar só de ida:", rs)