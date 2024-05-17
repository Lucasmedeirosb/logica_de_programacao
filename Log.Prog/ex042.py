#Faça um código que receba 4 números e realize a soma deles e a média entre eles e mostre o resultado
soma = 0
media = 0
for contador in range(4):
    num = int(input("Digite um número: "))
    soma = soma + num
media = soma/4
print("A soma dos números é:",soma)
print("A sua média é:",media)
