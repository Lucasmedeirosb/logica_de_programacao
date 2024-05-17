menu = 0

while menu != 3:
    menu = int(input("1 - Cálculo da área do triângulo\n2 - Cálculo da área do quadrado\n3 - Para Sair: "))

    if menu == 1:
        base = float(input("Digite o valor da base do triângulo: "))
        altura = float(input("Digite o valor da altura do triângulo: "))
        A = (base * altura) / 2
        print("A área do triângulo é:", A)
    elif menu == 2:
        lado = float(input("Digite o lado do quadrado: "))
        area_quadrado = lado ** 2
        print("A área do quadrado é:", area_quadrado)
    elif menu == 3:
        print("Você saiu do Programa!")
    else:
        print("Opção inválida")
