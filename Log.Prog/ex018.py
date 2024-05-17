#Ler 10 valores e escrever quantos desses valores lidos são negativos
neg=0
for i in range(10):
    n = int(input("Digite um número: "))
    if n < 0:
        neg = neg + 1
print(neg)
