num = int(input("Digite o número que você quer a tabuada: "))
for contador in range(1,11):
    mult = num * contador
    print("{} x {} = {}".format(num, contador, mult))