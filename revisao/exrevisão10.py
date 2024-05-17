#Faça um código que receba 4 números e realize a soma deles e a média entre eles. e mostre os resultados.
soma = 0
for contador in range(4):
    num = float(input(f"{contador + 1} - Digite um numero: "))
    soma = (soma + num)
    media = soma/4
print("A soma dos números foi:{} e a média entre eles foi:{}".format(soma,media))