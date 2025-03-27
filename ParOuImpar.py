'''Criar um jogo de par ou ímpar, onde dois jogadores entram com seu palpite (par ou
ímpar) e seus valores de 1 a 5. Tomar por base os nomes: Jogador 1 e Jogador 2. Caso
um dos valores esteja fora dos parâmetros informados, mostrar uma mensagem
informando que esta rodada não valeu. Caso contrário, informa qual jogador ganhou esta
rodada.'''

print("Jogo de Par ou Impar.")
escolha = input("Jogador 1 você é par ou impar?")
j1 = int(input("Escolha um número: "))
j2 = int(input("Escolha um número: "))
impar = [1, 3, 5, 7, 9]
soma = j1 + j2

if escolha == "impar" and soma in impar:
    print("Jogador 1 Ganhou!")
else:
    print("Jogador 2 Ganhou!")