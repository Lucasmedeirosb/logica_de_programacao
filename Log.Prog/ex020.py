#Ler 10 valores, calcular e escrever a média aritmética desses valores lidos
#as notas não podem estar fora do intevalo fora do 0 - 10
#
soma = 0
valor = 0
for contador in range(10):
    media=int(input("Digite os valores: "))
    soma = soma + media
valor = soma /10
print(valor)



