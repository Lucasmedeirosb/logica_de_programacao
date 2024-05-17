#Escreva um código que permita a leitura das notas de uma turma de 5 alunos e guarde nnum vetor, calcular a média
#da turma e contar quantos alunos obtiveram nota acima desta média calculada escrever a média da turma e o resultado da contagem
alunos = ["","","","",""]
media = 0
mediaTurma = 0
notaTotal = 0
aprovados = 0
for contador1 in range(len(alunos)):#declara
    alunos[contador1] = int(input("Digite as notas dos 5 alunos: "))#
for contador2 in range(0, len(alunos)):#soma os valores já armazenados
    notaTotal = notaTotal + alunos[contador2]
print(notaTotal)
media = (notaTotal)/len(alunos)
print(media)
for contador3 in range(0, len(alunos)):
    if alunos[contador3] >= media:
        aprovados = aprovados+1
print(f"A quantidade de alunos foi: {aprovados}")













