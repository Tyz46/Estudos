'''Criar um programa que pede ao usuário 5 números, e informa
qual é o menor e qual é o maior deles.'''

## Variaveis
lista = []
qtn = int(input('informe a qt de numeros: '))

## Adicionando os números escolhidos na Lista
for n in range(0, qtn):
    lista.append(int(input('Digite o número: ')))

## Resultado
print('Maior número da lista: ', max(lista))
print('Menor número da lista: ', min(lista))