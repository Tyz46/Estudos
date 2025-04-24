print("*** Cadastro de pessoas fudidas ***")
db = []
while True:
    name = input("Digite o nome da pessoa: ")
    age = int(input("Digite a idade da pessoa: "))
    city = input("Digite a cidade da pessoa: ")
    person = [name, age, city]
    db.append(person)
    resp = ("Deseja continuar? (s/n)")
    if resp == "n":
        break
print("*** Lista de pessoas fudidas ***")

for person in db:
    print(f"Nome: {person[0]}")
    print(f"Idade: {person[1]}")
    print(f"Cidade: {person[2]}")
    print()