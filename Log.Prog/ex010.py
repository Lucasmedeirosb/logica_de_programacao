n1 = int(input("Dogite um número: "))

if n1 == 0:
    print("numero inválido")
elif n1 % 2==0:
    print("{} é par".format(n1))
else:
    print(f"{n1} é ìmpar")