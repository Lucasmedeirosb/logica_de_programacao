#Crie um algoritmo que receba 3 npumeros e informa qual o maior entre eles
maiorNumero = 0
for contador in range(0,3,1):
    num = int(input(f"Digite o {contador+1} número: "))
    if num > maiorNumero:
        maiorNumero=num
print("o maior número é o:{} ".format(maiorNumero))

