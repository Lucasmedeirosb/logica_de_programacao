#Faça um código que receba 4 números e realize a soma deles e a média entre eles. e mostre os resultados.
soma = 0
for contador in range(4):
    num = int(input("Digite um número: "))
    soma = soma + num
print(soma/4)
