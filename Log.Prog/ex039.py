#Crie um algoritmo que receba 3 npumeros e informa qual o maior entre eles
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print("O maior número é: {}".format(n1))
elif n2 > n1 and n2 > n3:
    print("O maior número é: {}".format(n2))
elif n3 > n1 and n3 > n2:
    print("O maior número é: {}".format(n3))
