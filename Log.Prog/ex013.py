#n = int(input("Digite um número: "))

#for contador in range(0, 11, 1):
 #   t = n*contador
  #  print(f"{n}x{contador}={t}")

n = int(input("Digite um número: "))
resultado = 0
for k in range(1, 11):
    resultado = n * k
    print("{} x {} = {}".format(k,n, resultado))