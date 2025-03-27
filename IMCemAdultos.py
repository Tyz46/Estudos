'''O IMC – Índice de Massa Corporal é um critério da Organização Mundial de Saúde
para dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC
= peso / altura2 . Implemente um programa que leia o peso e a altura de um adulto e mostre
sua condição de acordo com a tabela abaixo.
IMC em adultos Condição
• Abaixo de 18,5 – Abaixo do peso
• Entre 18,5 e 25 – Peso normal
• Entre 25 e 30 – Acima do peso
• Acima de 30 – Obeso'''

peso = float(input("Qual seu peso? (Apenas número)"))
altura = float(input("Qual sua altura? (Somente número)"))
IMC = peso / (altura * altura)

if IMC <= 18.5:
    print("Abaixo do peso! Seu IMC é de:", "{:.2f}".format(round(IMC, 2)))
elif 18.5 < IMC <= 25:
    print("Peso normal! Seu IMC é de:", "{:.2f}".format(round(IMC, 2)))
elif 25 < IMC <= 30:
    print("Acima do peso! Seu IMC é de:", "{:.2f}".format(round(IMC, 2)))
elif IMC > 30:
    print("OBESO! Seu IMC é de:", "{:.2f}".format(round(IMC, 2)))
else:
    print("Você escreveu algo errado...")