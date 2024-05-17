#caso 1: se o usuario errar tosdas as notas
soma = 0
contador = 0
for i in range(10):
    num = float(input("Digite a nota: "))
    if num >=0 and num <=10:
        soma = soma + num
        contador = contador + 1
        print(soma)
if contador !=0:
    media = soma/contador
else:
    print("Digite corretamente")


#for x in range(10):
 #   num = int(input("Digite um número: "))
  #  print(f"Valor de x: {x}")
#print("x:", x)