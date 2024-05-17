#Preencher um vetor com A com 10 números logo em seguida ler mais um nummero e guardar em uma variavel X
#Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X, no final imprimir o vetor M
a = [0,0,0,0,0,0,0,0,0,0]
m = [0,0,0,0,0,0,0,0,0,0]
x = 0

for contador1 in range(len(a)):#declara
    a[contador1] = int(input("Digite as notas dos 10 alunos: "))
x = int(input("Digite o multiplicador: "))
for contador2 in range(len(a)):
    m[contador2] = a[contador2]*x
print(a)
print(x)
print(m)
