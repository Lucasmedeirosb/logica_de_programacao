#Escreva um codigo para ler as notas da 1 e 2 avaliação do aluno, caulcule e imprima a média
#desse aliuno só devem ser aceitos valores validos durante a leitura (0 a 10)para cada nota
#caso o usuario deseje um novo calculo, agora com o número de alunos
somamedia = 0
alunos = int(input("Quantos alunos tem na sala?: "))
for x in range(1, alunos+1):
    n1 = float(input("Digite a primeira nota: "))
    while n1 < 0 or n1 > 10:
        n1 = float(input("Digite a primeira nota válida: "))
    n2 = float(input("Digite a segunda nota: "))
    while n2 < 0 or n2 > 10:
        n2 = float(input("Digite a segunda nota válida: "))

    media = (n1+n1)/2
    print(media)
    somamedia = somamedia + media
media = somamedia/alunos
print("Média total da sala: ", media)

