#Crie um algoritmo que leia um número e diga se ele é par ou ímpar
outra = "S"
while outra == "S":
    num = int(input("Digite um número: "))
    if num %2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é impar")
    outra = input("Deseja fazer novamente?[S/N]")
    if outra == "N":
        print("Obrigado")