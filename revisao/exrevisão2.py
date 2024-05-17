#Crie um código que leia a idade de uma pessoa e diga em qual ano ela nasceu
outra = "S"
while outra == "S":
    ano_vigente = 2024
    idade = int(input("Digite a sua idade: "))
    aniversario = input("Você já fez aniversário este ano? (S/N): ")
    ano = ano_vigente - idade
    if aniversario.upper() == "N":
        ano = ano - 1  # Subtrai 1 do ano se o aniversário ainda não tiver ocorrido no ano atual
    print("Você nasceu em", ano)
    outra = input("Você deseja fazer um novo cálculo? (S/N): ").upper()
    if outra == "N":
        print("Obrigado por utilizar o programa!")
