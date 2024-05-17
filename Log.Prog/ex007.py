nome=(input("Digite o nome do Aluno: "))
n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
n3=float(input("Digite a terceira nota: "))
media = (n1+n2+n3)/3

if media>=7:
    print(f"{nome} Parabéns você foi Aprovado, sua média foi de {media}")
elif media>=4:
    print("Você está em Recuperação")
else:
    print(f"{nome} Você foi Reprovado")