#Crie um algoritmo que receba 3 números e informe qual o maior entre eles.
maiornumero = 0
for contador in range(3):
    num = int(input(f"Digite um número: "))
    if num > maiornumero:
        maiornumero = num
print(maiornumero)
