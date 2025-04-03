'''Criar um programa que solicita ao usuário 10 números, contando
quantos são pares e quantos são ímpares. Informar ao final estas
informações.'''

for i in range(10):
    n1 = int(input("Escolha um número: "))
    if n1 % 2 == 0:
        print("O número", n1, "é Par.")
    else:
        print("O número", n1, "é Impar.")