'''Criar um programa que recebe um texto digitado pelo usuário e
o imprime apenas com consoantes, removendo as vogais. Obs.:
desconsiderar letras maiúsculas e acentos.'''

string = input("Coloque um texto: ")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]

print(result)