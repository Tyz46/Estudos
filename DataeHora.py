'''Implemente um programa que solicite uma data com hora, pedindo em separado: dia,
mês, ano, hora, minuto e segundo. Pergunte ao usuário que informação ele deseja
acrescentar, e em qual quantidade. Informar a nova data de acordo com o solicitado pelo
usuário.
Ex.: Informada a data 31/12/2001 23:59:59, se o usuário pedir para acrescentar um
segundo a data deve ser exibida como 01/01/2002 00:00:00.
Para determinar se um ano é bissexto, execute estas etapas:
    1. Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá
para a etapa 5.
    2. Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário,
vá para a etapa 4.
    3. Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário,
vá para a etapa 5.
    4. O ano é bissexto (tem 366 dias).
    5. O ano não é um ano bissexto (tem 365 dias).'''

## Variaveis/Perguntas de Data e Hora
dia = int(input("Coloque um dia que desejar (Apenas números): "))
mes = int(input("Coloque um mês que desejar (Apenas números): "))
ano = int(input("Coloque um ano que desejar (Apenas números): "))

hora = int(input("Que horas? (Apenas números): "))
min = int(input("Quantos minutos? (Apenas números): "))
seg = int(input("Quantos segundos? (Apenas números): "))

## Data e Hora escolhidas
print("Está é a Data que você escolheu: ", dia, "/", mes, "/", ano, sep='')
print("Este é o Horário que você escolheu: ", hora, ":", min, ":", seg, sep='')

## Variaveis/Perguntas de Alteração
ask1 = input("Deseja alterar alguma coisa da Data? (Dia, Mês ou Ano / Não): ")
qntd1 = int(input("Quanto quer adicionar? (Apenas números, digite 'Não' se não quiser alterar): "))
ask2 = input("Deseja alterar alguma coisa da Hora? (Hora, Minuto ou Segundo / Não): ")
qntd2 = int(input("Quanto quer adicionar? (Apenas números, digite 'Não' se não quiser alterar): "))

## Condições de Data
if ask1 == "Dia":
    dia = dia + qntd1
    print("Está é a Nova Data que você escolheu: ", dia, "/", mes, "/", ano, sep='')
elif ask1 == "Mês":
    mes = mes + qntd1
    print("Está é a Nova Data que você escolheu: ", dia, "/", mes, "/", ano, sep='')
elif ask1 == "Ano":
    ano = ano + qntd1
    if ano / 4:
        if ano / 100:
            if ano / 400:
                print("Está é a Nova Data que você escolheu: ", dia, "/", mes, "/", ano, sep='')
                print("O ano é bissexto.")
            else:
                print("Está é a Nova Data que você escolheu: ", dia, "/", mes, "/", ano, sep='')
                print("O ano não é um ano bissexto.")
        else:
            print("Está é a Nova Data que você escolheu: ", dia, "/", mes, "/", ano, sep='')
            print("O ano é bissexto.")
    else:
        print("Está é a Nova Data que você escolheu: ", dia, "/", mes, "/", ano, sep='')
        print("O ano não é um ano bissexto.")
else:
    print("Data não alterada.")

## Condições de Hora
if ask2 == "Hora":
    hora = hora + qntd2
    if hora >= 23:
        hora = hora - 22
        print("Este é o Novo Horário que você escolheu: ", "00", ":", min, ":", seg, sep='')
    else:
        print("Este é o Novo Horário que você escolheu: ", hora, ":", min, ":", seg, sep='')
elif ask2 == "Minuto":
    min = min + qntd2
    if min >= 60:
        hora2 = hora + 1
        min = min - 60
        if hora2 >= 23:
            hora2 = hora - 22
            print("Este é o Novo Horário que você escolheu: ", "00", ":", "00", ":", "00", sep='')
        else:
            print("Este é o Novo Horário que você escolheu: ", hora2, ":", "00", ":", "00", sep='')
    else:
        print("Este é o Novo Horário que você escolheu: ", hora, ":", min, ":", seg, sep='')
elif ask2 == "Segundo":
    seg = seg + qntd2
    if seg >= 60:
        min2 = min + 1
        seg = seg - 60
        if min2 >= 60:
            hora2 = hora + 1
            min2 = min2 - 60
            if hora2 >= 23:
                hora2 = hora - 22
                print("Este é o Novo Horário que você escolheu: ", "00", ":", "00", ":", "00", sep='')
            else:
                print("Este é o Novo Horário que você escolheu: ", hora2, ":", "00", ":", "00", sep='')
        else:
            print("Este é o Novo Horário que você escolheu: ", hora, ":", "00", ":", "00", sep='')
    else:
        print("Este é o Novo Horário que você escolheu: ", hora, ":", min, ":", seg, sep='')
else:
    print("Hora não alterada.")