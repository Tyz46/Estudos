## Data e Exibição:

dia = int(input("Em que dia você nasceu? (Apenas números)"))
mes1 = int(input("Em que mês você nasceu? (Apenas números)"))
mes2 = input("Coloque o mês por escrito agora.")
ano = int(input("Coloque o ano em que você nasceu. (Apenas números): "))

print("Primeiro Exemplo: 10/08/1990")
print("Segundo Exemplo: 10/ago/1990")
print("Terceiro Exemplo: 10 de agosto de 1990")
exibicao = input("Me diga como você gostaria que fosse exibida a data. (Primeiro, Segundo ou Terceiro): ")

meses_ab = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'ago', 'set', 'out', 'nov', 'dez']

## Condições:

if exibicao == "Primeiro":
    print("Você nasceu em: ", dia, "/", mes1, "/", ano, sep='')
elif exibicao == "Segundo":
    if mes2 == "janeiro":
        mes2 = meses_ab[0]
        print("Você nasceu em: ", dia, "/", mes2, "/", ano, sep='')
    elif mes2 == "fevereiro":
        mes2 = meses_ab[1]
        print("Você nasceu em: ", dia, "/", mes2, "/", ano, sep='')
    elif mes2 == "março":
        mes2 = meses_ab[2]
        print("Você nasceu em: ", dia, "/", mes2, "/", ano, sep='')
    elif mes2 == "abril":
        mes2 = meses_ab[3]
        print("Você nasceu em: ", dia, "/", mes2, "/", ano, sep='')
    elif mes2 == "maio":
        mes2 = meses_ab[4]
        print("Você nasceu em: ", dia, "/", mes2, "/", ano, sep='')
    elif mes2 == "junho":
        mes2 = meses_ab[5]
        print("Você nasceu em: ", dia, "/", mes2, "/", ano, sep='')
    elif mes2 == "julho":
        mes2 = meses_ab[6]
        print("Você nasceu em: ", dia, "/", mes2, "/", ano, sep='')
    elif mes2 == "agosto":
        mes2 = meses_ab[7]
        print("Você nasceu em: ", dia, "/", mes2, "/", ano, sep='')
    elif mes2 == "setembro":
        mes2 = meses_ab[8]
        print("Você nasceu em: ", dia, "/", mes2, "/", ano, sep='')
    elif mes2 == "outubro":
        mes2 = meses_ab[9]
        print("Você nasceu em: ", dia, "/", mes2, "/", ano, sep='')
    elif mes2 == "novembro":
        mes2 = meses_ab[10]
        print("Você nasceu em: ", dia, "/", mes2, "/", ano, sep='')
    elif mes2 == "dezembro":
        mes2 = meses_ab[11]
        print("Você nasceu em: ", dia, "/", mes2, "/", ano, sep='')
    else:
        print("algo deu errado 2")
elif exibicao == "Terceiro":
    print("Você nasceu em: ", dia, "de", mes2, "de", ano, sep='')
else:
    print("algo deu errado 1")