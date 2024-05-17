#Faça um código para ler a senha de um usuario e apos 3 tentativas erradas sair do programa,
#informando que a senha esá bloqueada
tentativas = 0
senha = 123456
campo = int(input("Digite a sua senha: "))

if senha == campo:
    print("Bem-Vindo")
else:
    while senha != campo and tentativas < 2:
        campo = int(input("Senha incorreta. Digite novamente a sua senha: "))
        tentativas = tentativas + 1
if senha == campo:
    print("Bem-Vindo")
else:
    print("Senha Bloqueada por excesso de tentativas!")




