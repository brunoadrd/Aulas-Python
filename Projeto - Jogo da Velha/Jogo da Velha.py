import random
import pdb
import os

class JogoVelha:
    lista_jogadores = []

    def __init__(self):
        self.inicializar()
        self.finalizar = 0

    def posicoes_disponiveis(self):
        a = [(i, self.matriz[i]) for i, x in enumerate(self.matriz) if x not in ["X", "O"]]
        return [x for x, y in a]
    
    def jogar(self, pos, jogador):
        if (jogador == 1):
            self.matriz[pos] = "X"
        else: self.matriz[pos] = "O"
        os.system("cls")
        self.mostrar_jogo()
        self.finalizar_jogo()

    def posicao_pc(self):
        return random.choice(self.posicoes_disponiveis())
    
    def finalizar_jogo(self):
        if (self.matriz[0] == self.matriz[1] == self.matriz[2]):
            if self.matriz[0] == "X":
                print("Jogador 1, venceu o jogo!")
            else:
                print("Jogador 2, venceu o jogo!")
            self.finalizar = 1

        elif (self.matriz[3] == self.matriz[4] == self.matriz[5]):
            if self.matriz[3] == "X":
                print("Jogador 1, venceu o jogo!")
            else:
                print("Jogador 2, venceu o jogo!")
            self.finalizar = 1

        elif (self.matriz[6] == self.matriz[7] == self.matriz[8]):
            if self.matriz[6] == "X":
                print("Jogador 1, venceu o jogo!")
            else:
                print("Jogador 2, venceu o jogo!")
            self.finalizar = 1

        elif (self.matriz[0] == self.matriz[3] == self.matriz[6]):
            if self.matriz[0] == "X":
                print("Jogador 1, venceu o jogo!")
            else:
                print("Jogador 2, venceu o jogo!")
            self.finalizar = 1

        elif (self.matriz[1] == self.matriz[4] == self.matriz[7]):
            if self.matriz[1] == "X":
                print("Jogador 1, venceu o jogo!")
            else:
                print("Jogador 2, venceu o jogo!")
            self.finalizar = 1

        elif (self.matriz[2] == self.matriz[5] == self.matriz[8]):
            if self.matriz[2] == "X":
                print("Jogador 1, venceu o jogo!")
            else:
                print("Jogador 2, venceu o jogo!")
            self.finalizar = 1

        elif (self.matriz[0] == self.matriz[4] == self.matriz[8]):
            if self.matriz[0] == "X":
                print("Jogador 1, venceu o jogo!")
            else:
                print("Jogador 2, venceu o jogo!")
            self.finalizar = 1

        elif (self.matriz[2] == self.matriz[4] ==  self.matriz[6]):
            if self.matriz[2] == "X":
                print("Jogador 1, venceu o jogo!")
            else:
                print("Jogador 2, venceu o jogo!")
            self.finalizar = 1

        elif (len(self.posicoes_disponiveis()) == 0):
            print("Deu velha!")
            self.finalizar = 1

    def mostrar_jogo(self):
        tela = ""

        for i in range(9):
            if (i in [2, 5, 8]):
                print(tela + "{}".format(self.matriz[i]))
                if i != 8:
                    print("_________")
                    tela = ""
                else: print("\n")
            else:
                tela += "{} | ".format(self.matriz[i])

    def inicializar(self):
        print("=======================")
        print("Jogo da Velha iniciado!")
        print("=======================\n")

        print("Escolha a posição da sua jogada com base nos campos onde há números!")
        self.matriz = [i+1 for i in range(9)]
        self.mostrar_jogo()

    def reiniciar_jogo(self):
        print("Deseja reiniciar o jogo?")
        print("1 - Sim | 2 - Não (Sair)")

        reiniciar = int(input())

        if (reiniciar == 1):
            os.system("cls")
            self.inicializar()
            self.finalizar = 0
        else:
            return "Parar"

class Jogador:
    def __init__(self, jogo, jogador = "Computador"):
        if jogador not in [1, 2, "Computador"]:
            raise Exception("Escolha um jogador válido: 1, 2, ou vazio para jogar contra o Computador.")

        self.jogador = jogador
        self.jogo = jogo
        
        jogo.lista_jogadores.append(self)

    def jogar(self, pos = -1):
        if self.jogador == "Computador":
            jogo.jogar(jogo.posicao_pc(), self.jogador)
        else:         
            jogo.jogar(pos-1, self.jogador)

jogo = JogoVelha()
jogador1 = Jogador(jogo, 1)
jogador2 = Jogador(jogo)

x = ""

while x != "Parar":
    for jogador in JogoVelha.lista_jogadores:
        if jogo.finalizar == 0:
            if (jogador.jogador != "Computador"):
                pos = int(input())
                while((pos not in [i for i in range(1, 10)]) or ((pos-1) not in jogo.posicoes_disponiveis())):
                    print("Digite uma jogada válida!")
                    pos = int(input())
                jogador.jogar(pos)
            else:
                jogador.jogar()
    if jogo.finalizar == 1:   
        x = jogo.reiniciar_jogo()
