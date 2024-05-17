#Crie um código que leia a idade de uma pessoa e diga quak ano ela nasceu
outra = "S"
while outra == "s" or outra == "S":
    anoVigente = 2024
    idade = int(input("Digite a sua idade: "))
    aniversario = input("Você já fez aniverrsário?")
    calculo = anoVigente - idade
    if aniversario == "N" or aniversario == "n":
        calculo -= 1
    print(f"Você nasceu no ano: {calculo}")
    outra = input("Você deseja consultar novamente? Digite [S/N]").upper()
    if outra == "N":
        print("Obrigado!")
