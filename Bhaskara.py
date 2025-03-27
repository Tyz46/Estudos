'''Implemente um programa para calcular as raízes de uma equação do 2º grau, sendo que
os valores dos coeficientes A, B, e C devem ser fornecidos pelo usuário, e os valores das
raízes devem ser calculadas pela fórmula de Bhaskara, como segue:'''

print("Vamos fazer Bhaskara, digite os números")
n1 = int(input("Coloque o número do A: "))
n2 = int(input("Coloque o número do B: "))
n3 = int(input("Coloque o número do C: "))
delta = (n2 * n2) - (4 * ((n1) * (n3)))

raiz = float(delta) ** 0.5

b1 = (-n2 + raiz) / (2 * n1)
b2 = (-n2 - raiz) / (2 * n1)
print("Valores da Equação:", b1, b2)