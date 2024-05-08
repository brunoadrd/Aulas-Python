import random

class Academia():
    def __init__(self):
        self.halteres = [i for i in range(5, 36 + 1) if i % 2 == 0]
        self.pos_halteres = {}
        self.reiniciar_dia()

    def reiniciar_dia(self):
        self.pos_halteres = {i: i for i in self.halteres}

    def halteres_disponiveis(self):
        return [i for i in self.pos_halteres.values() if i != 0]
    
    def pos_disponiveis(self):
        return [i for i, x in self.pos_halteres.items() if x == 0]
    
    def pegar_halter(self, peso):
        posicao_halter = list(self.pos_halteres.values()).index(peso)
        chave_posicao = list(self.pos_halteres.keys())[posicao_halter]

        self.pos_halteres[chave_posicao] = 0

    def devolver_halter(self, pos, peso):
        self.pos_halteres[pos] = peso

    def calcular_caos(self):
        caos = [i for i, x in self.pos_halteres.items() if i != x]
        valor_caos = len(caos) / len(self.halteres) * 100

        return valor_caos
    
class Pessoa():
    def __init__(self, caotico, academia):
        self.caotico = caotico
        self.academia = academia
        self.peso = 0

    def pegar_halter(self):
        self.peso = random.choice(self.academia.halteres_disponiveis())
        self.academia.pegar_halter(self.peso)

    def devolver_halter(self):
        posicao = self.academia.pos_disponiveis()

        if (self.caotico == 1):
            self.academia.devolver_halter(random.choice(posicao), self.peso)

        else:
            if (self.peso in posicao):
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                self.academia.devolver_halter(random.choice(posicao), self.peso)
        


academia = Academia()

usuarios = [Pessoa(0, academia) for i in range(9)]
usuarios += [Pessoa(1, academia) for i in range(1)]
random.shuffle(usuarios)

somar_caos = []


for k in range(50):
    academia.reiniciar_dia()
    for i in range(10):
        random.shuffle(usuarios)

        for usuario in usuarios:
            usuario.pegar_halter()

        for usuario in usuarios:
            usuario.devolver_halter()

    somar_caos += [academia.calcular_caos()]