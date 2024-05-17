# Escreva um algoritmo para ler a hora de inicio e a hora de fim de um jogo de xadrez(considere apenas horas inteiras sem os minutos)
# e calcule a duração do jogo em horas sabendo q o tempo maximo de diração do jogo é de 24horas
# e que o jogo pode iniciar em um dia e terminar no dia seguinte
inicio = int(input("Digite a hora de início: "))
final = int(input("Digite a hora de Térrmino: "))
if inicio<=final:
    duracao=final-inicio
else:
    duracao=(24-inicio)+final
print(duracao)