import os
import random
import pdb

pontos_usuario = 0
pontos_pc = 0
lances = ["Pedra", "Papel", "Tesoura"]
sair = False

def placar(pontos_usuario, pontos_pc):
    print("=================")
    print("PLACAR:")
    print("Você: {}".format(pontos_usuario))
    print("Computador: {}".format(pontos_pc))
    print("=================\n")

def verifica_vencedor(lance_usuario, lance_computador, pontos_usuario, pontos_pc):
    os.system("cls")

    if (lance_usuario == lance_computador):
        print('Empate! Você escolheu: "{}" e o Computador escolheu: "{}"'.format(lances[lance_usuario], lances[lance_computador]))
        return [pontos_usuario, pontos_pc]
    
    elif ((lance_usuario == 0) and (lance_computador == 1)):
        print('Poxa, você perdeu! Você escolheu: "{}" e o Computador escolheu: "{}"'.format(lances[lance_usuario], lances[lance_computador]))
        pontos_pc += 1
        return [pontos_usuario, pontos_pc]
    elif ((lance_usuario == 0) and (lance_computador == 2)):
        print('Parabéns, você ganhou! Você escolheu: "{}" e o Computador escolheu: "{}"'.format(lances[lance_usuario], lances[lance_computador]))
        pontos_usuario += 1
        return [pontos_usuario, pontos_pc]
    
    elif ((lance_usuario == 1) and (lance_computador == 0)):
        print('Parabéns, você ganhou! Você escolheu: "{}" e o Computador escolheu: "{}"'.format(lances[lance_usuario], lances[lance_computador]))
        pontos_usuario += 1
        return [pontos_usuario, pontos_pc]

    elif ((lance_usuario == 1) and (lance_computador == 2)):
        print('Poxa, você perdeu! Você escolheu: "{}" e o Computador escolheu: "{}"'.format(lances[lance_usuario], lances[lance_computador]))
        pontos_pc += 1
        return [pontos_usuario, pontos_pc]

    elif ((lance_usuario == 2) and (lance_computador == 0)):
        print('Poxa, você perdeu! Você escolheu: "{}" e o Computador escolheu: "{}"'.format(lances[lance_usuario], lances[lance_computador]))
        pontos_pc += 1
        return [pontos_usuario, pontos_pc]

    elif ((lance_usuario == 2) and (lance_computador == 1)):
        print('Parabéns, você ganhou! Você escolheu: "{}" e o Computador escolheu: "{}"'.format(lances[lance_usuario], lances[lance_computador]))
        pontos_usuario += 1
        return [pontos_usuario, pontos_pc]

while True:
    os.system('cls')

    placar(pontos_usuario, pontos_pc)

    print("Escolha seu lance:")
    print("1 - Pedra | 2 - Papel | 3 - Tesoura")

    while True:
        try:
            lance_usuario = int(input()) - 1
            if lance_usuario not in [0, 1, 2]:
                raise
            break
        except Exception as e:
            print(e)
        
    lance_computador = random.choice(lances)

    pontos = verifica_vencedor(lance_usuario, lances.index(lance_computador), pontos_usuario, pontos_pc)
    pontos_usuario = pontos[0]
    pontos_pc = pontos[1]

    print("Deseja continuar?")
    print("1 - Sim | 2 - Não (Sair)")

    while True:
        try:
            sair = int(input())
            if sair not in [1, 2]:
                raise
            break
        except Exception as e:
            print(e)

    if (sair == 2):
        break