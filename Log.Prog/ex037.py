#Crie um código que leia um número diferente de zero e diga se este nnúmero é positivo ou negativo
outra = "S"
while outra == "S" or outra == "s":

    num = int(input("Digite um número: "))
    while num == 0:
        num = int(input("Digite um número válido: "))
    if num < 0:
        print("Esse número é negativo")
    else:
        print("Esse é positivo")
    outra = input("Deseja realizar novamente? digite S para sim e N para não")
    if outra == "N" or outra == "n":
        print("Obrigado!")



