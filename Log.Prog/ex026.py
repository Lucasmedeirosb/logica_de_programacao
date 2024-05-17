#Escreva um codigo para ler as notas da 1 e 2 avaliação do aluno, caulcule e imprima a média
#desse aliuno só devem ser aceitos valores validos durante a leitura (0 a 10)para cada nota
#caso o usuario deseje um novo calculo
n3 = "S"
while n3 == "S" or n3 == "s":
    n1 = float(input("Digite a primeira nota: "))
    media = 0
    while n1 < 0 or n1 > 10:
        n1 = float(input("Digite a primeira nota válida: "))
    n2 = float(input("Digite a segunda nota: "))
    while n2 < 0 or n2 > 10:
        n2 = float(input("Digite a segunda nota válida: "))
    media = (n1+n1)/20
    print(media)
    n3 = input("Deseja realizar um novo cálculo? digite S para sim e N para não")
    if n3 == "N" or n3 == "n":
        print("Obrigado!")






