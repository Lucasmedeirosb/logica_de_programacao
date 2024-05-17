#receba do usuario um numero de 1 a 12 e mostr o nome do mes correspondente caso o mes nao exista mostrar valor invalido
m = int(input("Digite um número de 1 a 12: "))

if m > 1 or m < 12:
    print("Digite um número válido")

elif m == 1:
    print("Janeiro")
elif m == 2:
    print("Fevereiro")
elif m == 3:
    print("Março")
elif m == 4:
    print("Abril")
elif m == 5:
    print("Maio")
elif m == 6:
    print("Junho")
elif m == 7:
    print("Julho")
elif m == 8:
    print("Agosto")
elif m == 9:
    print("Setembro")
elif m == 10:
    print("Outubro")
elif m == 11:
    print("Novembro")
elif m == 12:
    print("Dezembro")
#else:
    #print("Número iválido")

