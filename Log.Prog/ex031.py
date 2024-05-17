#Criar um array tamanho 5 e preencher com os nomes dos 5 alunos, informados pelo usuario
alunos = ["","","","",""]
for x in range(len(alunos)):#pode usar (5) também
    alunos[x] = input("Digite 5 nomes: ")#
for i in range(len(alunos)):
    print(alunos[i], end= ", ")





