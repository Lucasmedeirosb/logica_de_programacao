time1=(input("Digite o nome do Time: "))
gol1=int(input("Digite o número de gols: "))
time2=(input("Digite o nome do Time: "))
gol2=int(input("Digite o número de gols: "))


if gol1 == gol2:
    print("Empate")

elif gol1 > gol2:
    print(f"{time1} foi o vencedor")

else:
    print(f"{time2} foi o perdedor")

