#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa
#expressa em apenas em dias, considerar ano com 365 dias e mês com 30 dias
print("Digite a sua idade")
ano = int(input("Digite o seu ano: "))
mes = int(input("Digite a sua mês: "))
dia = int(input("Digite a sua dias: "))
print((ano*365)+(mes*30)+dia)
