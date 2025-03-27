'''Tendo como dados de entrada a altura e o sexo de uma pessoa, implemente um
programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
• para homens: (72.7 * h) – 58;
• para mulheres: (62.1 * h) – 44.7.'''

sexo = input("Qual seu sexo? (F ou M): ")
altura = float(input("Qual sua altura? (Somente número)"))
homens = (72.7 * altura) - 58
mulheres = (62.1 * altura) - 44.7

if sexo == "M":
    print(homens)
else:
    print(mulheres)