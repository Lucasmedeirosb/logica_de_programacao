litro=float(input("Digite a quantidade de litros  que você colocou: "))
combustivel=input("Digite o combustivél que voccê colocou\n G=gasolina \n E=etanol\n")
precofinal=0

if combustivel == "G":
    precofinal = litro * 5.80
    print("O valor final da Gasolina foi: ",precofinal)

else:
    precofinal = litro * 4.90
    print(f"O valor final do E-tanol foi: {precofinal}")