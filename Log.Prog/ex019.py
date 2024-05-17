#Ler 10 valores e eocrever quantos desses valores lidps estãp no intervalo [10, 20]
intervalo = 0
fora = 0
#Sempre inicializar uma variavél, boa prática de prog
for contador in range(11, 21, 1):
    n = int(input("Digite um número: "))

    if n <= 20 and n >= 10:
       intervalo = intervalo + 1
    #else:
fora = 10 - intervalo
print(intervalo, fora)
