#Faça um codigo que receba o número de alunos de uma sala de aula e depois solicite
# as notas desses alunos, no final, mostre a média aritmética da turma

alunos = 0
soma = 0
nota = int(input("Digite o número de alunos nna sala: "))
while alunos < nota:
    b = float(input("Digite um número: "))
    soma = soma + b
    alunos = alunos + 1

media = soma / alunos
print(soma, alunos, media)