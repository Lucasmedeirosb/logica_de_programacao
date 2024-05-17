#15. Escreva um algoritmo para ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
while n1 == n2:
    print("Escreva números diferentes!")
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
print(n1+n2)