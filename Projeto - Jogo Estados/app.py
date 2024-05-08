import random
import os
import pdb

class Jogo:
    def __init__(self):
        self.capitais_estados = {
            "Acre" : "Rio Branco",
            "Alagoas" : "Maceió",
            "Amapá" : "Macapá",
            "Amazonas" : "Manaus",
            "Bahia" : "Salvador",
            "Ceará" : "Fortaleza",
            "Espírito Santo" : "Vitória",
            "Goiás" : "Goiânia",
            "Maranhão" : "São Luís",
            "Mato Grosso" : "Cuiabá",
            "Mato Grosso do Sul" : "Campo Grande",
            "Minas Gerais" : "Belo Horizonte",
            "Pará" : "Belém",
            "Paraíba" : "João Pessoa",
            "Paraná" : "Curitiba",
            "Pernambuco" : "Recife",
            "Piauí" : "Teresina",
            "Rio de Janeiro" : "Rio de Janeiro",
            "Rio Grande do Norte"  : "Natal",
            "Rio Grande do Sul"  : "Porto Alegre",
            "Rondônia" : "Porto Velho",
            "Roraima" : "Boa Vista",
            "Santa Catarina" : "Florianópolis",
            "São Paulo" : "São Paulo",
            "Sergipe" : "Aracaju",
            "Tocantins" : "Palmas"
        }
        self.acertos = 0
        self.erros = 0
        self.desafio = ""
        self.mensagem_tentativa = ""

    def mostrar_jogo(self):
        os.system("cls")

        print("|============================|                Sua pontuação")
        print("|Acerte a capital dos estados|                Acertos: {}".format(self.acertos))
        print("|============================|                Erros: {}\n".format(self.erros))
        
        print(f'Desafio: "{self.desafio}"')
        print(self.mensagem_tentativa)
    
    def jogar(self, capital):
        if capital.lower() == self.capitais_estados[self.desafio].lower():
            self.mensagem_tentativa = "Parabéns, você acertou a capital do estado {} é {}!\n".format(self.desafio, self.capitais_estados[self.desafio])
            self.adicionar_acerto()
            return "Acertou"
        else:
            self.mensagem_tentativa = "Incorreto, esta não é a capital do estado {}!\n".format(self.desafio)
            self.adicionar_erro()

    def adicionar_acerto(self):
        self.acertos += 1

    def adicionar_erro(self):
        self.erros += 1

    def gerar_desafio(self):
        lista_estados = list(self.capitais_estados.keys())
        self.desafio = random.choice(lista_estados)

    def reiniciar(self, opcao):
        if (opcao == 1):
            self.gerar_desafio()
            self.mostrar_jogo()
            self.mensagem_tentativa = ""
    
jogo = Jogo()
jogo.gerar_desafio()

while True:
    fimjogo = ""
    jogo.mostrar_jogo()

    while (fimjogo != "Acertou"):
        
        tentativa = input()
        fimjogo = jogo.jogar(tentativa)
        jogo.mostrar_jogo()

    jogo.mostrar_jogo()
    print("Digite 1 para continuar, ou qualquer tecla para sair do Jogo.")
    
    sair = input()
    
    if (sair != 1):
        break
    else:
        jogo.reiniciar(sair)