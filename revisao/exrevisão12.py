#17.As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que
#leia o número de maçãs compradas, calcule e escreva o custo total da compra.
soma = 0
num = int(input("Digite a quantidade de maças que você quer: "))
if num < 12:
    soma = num * 1.30
    print("Você adicionou {} maçãs ao carrinho, o valor total é de: R${}".format(num, soma))
else:
    soma = num * 1.00
    print("Você adicionou {} maçãs ao carrinho e garantiu o desconto, o valor total é de: R${}".format(num, soma))