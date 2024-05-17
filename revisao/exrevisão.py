#Crie um código que leia um número diferente de zero e diga se este número é positivo ou negativo
num = int(input("Digite um número: "))
while num == 0:
    num = int(input("Digite um número diferente de zero: "))
if num >= 0:
    print("{} é positivo!".format(num))
else:
    print("{} é negativo!".format(num))