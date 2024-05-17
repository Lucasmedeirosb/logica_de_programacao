#Faça um código para ler 5 números e armazenar em um vetor. Após a leitura total dos 5 números
# o código deve escrever esses 5 números lidos na ordem inversa.
num=[0,0,0,0,0]
for contador1 in range(len(num)):#declara
    num[contador1] = int(input("Digite 5 números: "))
    print(num)
for contador2 in range(len(num)-1, -1, -1): #(4, -1, -1):
    print(num[contador2], end=", ")


