#ler 10 valores, calcular e escrever a média aritmética
x=0
soma = 0
while x<10:
    print(f"Vakor de x: {x}")
    n = float(input("Digite um número: "))
    soma = soma + n
    x = x + 1
    print(f"Valor final de {x}")

media = soma / 10
print(media)