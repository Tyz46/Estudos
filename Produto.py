'''Implemente um programa que calcule o que deve ser pago por um produto,
considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize
os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o
cálculo adequado.
Código Condição de pagamento
• 1 – À vista em dinheiro ou cheque, recebe 10% de desconto
• 2 – À vista no cartão de crédito, recebe 15% de desconto
• 3 – Em duas vezes, preço normal de etiqueta sem juros
• 4 – Em duas vezes, preço normal de etiqueta mais juros de 10%'''

produto = input("O que você está comprando? (Produto): ")
quantidade = int(input("Quantos desse produto você está comprando? (Apenas números): "))
valor = float(input("Qual o valor do produto? (Apenas números): "))
f_pgmnt = input("Como você deseja pagar? (Dinheiro, Cheque, ou Cartão de Crédito): ")

qntd = valor * quantidade
desconto1 = 10 * qntd / 100
desconto2 = 15 * qntd / 100

if f_pgmnt == "Cartão de Crédito":
    ask = input("Você quer parcelar em 2 vezes? (Sim ou Não?): ")
    if ask == "Sim":
        valor1 = qntd - desconto2
        valor_total = valor1 - desconto1
        print("O valor total a pagar do produto", produto, "com desconto e juros é:", valor_total)
    else:
        valor_total = qntd - desconto2
        print("O valor total a pagar do produto", produto, "com desconto é:", valor_total)
else:
    if f_pgmnt == "Dinheiro" or "Cheque":
        valor_total = qntd - desconto1
        print("O valor total a pagar do produto", produto, "com desconto é:", valor_total)
    else:
        print("Algo deu errado.")