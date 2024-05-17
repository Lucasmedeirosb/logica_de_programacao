soma = 0
nota = 0
for contador in range(0,2,1):
    nota = int(input(f"Digite a {contador+1} nota: "))
    while nota > 10 or nota < 0:
        input("Nota inválida, digite novamente")
    soma = nota+nota
media = soma/2
print(media)
