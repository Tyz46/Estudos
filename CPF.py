'''9. Implementar um programa que valide um CPF. Para tanto, solicitar em separado cada
um dos 11 dígitos do CPF.

Definição
O CPF é formado por 11 dígitos numéricos que seguem a máscara "###.###.###-##", a
verificação do CPF acontece utilizando os 9 primeiros dígitos e, com um cálculo simples,
verificando se o resultado corresponde aos dois últimos dígitos (depois do sinal "-").
Vamos usar como exemplo, um CPF fictício "529.982.247-25".

Validação do primeiro dígito
Primeiramente multiplica-se os 9 primeiros dígitos pela sequência decrescente de
números de 10 à 2 e soma os resultados. Assim:
5 * 10 + 2 * 9 + 9 * 8 + 9 * 7 + 8 * 6 + 2 * 5 + 2 * 4 + 4 * 3 + 7 * 2
O resultado do nosso exemplo é: 295

O próximo passo da verificação também é simples, basta multiplicarmos esse resultado
por 10 e dividirmos por 11.
295 * 10 / 11

O resultado que nos interessa na verdade é o RESTO da divisão. Se ele for igual
ao primeiro dígito verificador (primeiro dígito depois do '-'), a primeira parte da
validação está correta.

Observação Importante: Se o resto da divisão for igual a 10, nós o consideramos como
0.
O resultado da divisão acima é '268' e o RESTO é 2
Isso significa que o nosso CPF exemplo passou na validação do primeiro dígito.
'''

n1 = int(input("Digite o primeiro número do seu CPF: "))
n2 = int(input("Digite o segundo número do seu CPF: "))
n3 = int(input("Digite o terceiro número do seu CPF: "))
n4 = int(input("Digite o quarto número do seu CPF: "))
n5 = int(input("Digite o quinto número do seu CPF: "))
n6 = int(input("Digite o sexto número do seu CPF: "))
n7 = int(input("Digite o sétimo número do seu CPF: "))
n8 = int(input("Digite o oitavo número do seu CPF: "))
n9 = int(input("Digite o nono número do seu CPF: "))
n10 = int(input("Digite o décimo número do seu CPF: "))
n11 = int(input("Digite o décimo primeiro número do seu CPF: "))

calc1 = (n1 * 10) + (n2 * 9) + (n3 * 8) + (n4 * 7) + (n5 * 6) + (n6 * 5) + (n7 * 4) + (n8 * 3) + (n9 * 2)
calc2 = (calc1 * 10)

if calc2 % 11 == n10:
    calc3 = calc2 % 11
    if calc2 % 11 == 10:
        calc2 = 0
        print("A primeira parte da verificação está correta:", calc2)
    else:
        print("A primeira parte da verificação está correta:", calc3)
else:
    print("Você deve ter digitado algo errado.")