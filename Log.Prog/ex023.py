#faça um código para ler 2 valores e realize a divisão do primeiro pelo segundo valor recebido, caso o segundo valor digitado,
#seja zero solicite novamente o valor indormado que só aceitaremos valor diferente de zero
n1 = int(input("digite o primeiro número: "))
n2 = int(input("digite o segundo néumero: "))

while n2 == 0:
    n2 = int(input("Digite um valor diferente do zero: "))

divisao = n1/n2
print(f"O valor da divisão é: {divisao}")