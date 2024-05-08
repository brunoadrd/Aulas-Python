
import os

lista_carros = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130)
]

carros_alugados = []

def listarcarros(lista_carros):
    for i, carros in enumerate(lista_carros):
        print("[{}] {} - R$ {} / dia.".format(i + 1, carros[0], carros[1]))


while True:
    os.system("cls")
    print("O que deseja fazer?")
    print("1 - Mostrar portifólio | 2 - Alugar um Carro | 3 - Devolver um carro")
    opcao = int(input())

    os.system("cls")

    if (opcao == 1):
        listarcarros(lista_carros)

    elif (opcao == 2):
        listarcarros(lista_carros)

        print("\nDigite o código do carro:")
        codigo_carro = int(input()) - 1

        print("\nPor quantos dias deseja alugar?")
        dias_aluguel = int(input())

        os.system("cls")

        print("Você escolheu {} por {} dias".format(lista_carros[codigo_carro][0], dias_aluguel))
        print("O aluguel total é de R$ {:.2f}. Deseja confirmar a locação?".format(lista_carros[codigo_carro][1] * dias_aluguel))
        print("1 - Sim | 2 - Não")
        alugado = int(input())

        if alugado == 1:
            print("Parabéns por ter alugado o {} por {} dias.".format(lista_carros[codigo_carro][0], dias_aluguel))
            carros_alugados.append(lista_carros.pop(codigo_carro))
        else: print("Poxa, que pena. Fica pra próxima!")

    elif (opcao == 3):

        if carros_alugados == []: 
            print("Não há carros para serem devolvidos.")
        else:
            listarcarros(carros_alugados)

            print("Digite o código do carro que deseja devolver.")
            codigo_carro = int(input()) - 1

            if (-1 < codigo_carro < len(carros_alugados)):
                print("\nTem certeza que deseja devolver este veículo?")
                print("1 - Sim | 2 - Não")

                if (int(input()) == 1): 
                    os.system("cls")
                    print("Obrigado, confirmamos que o carro {} foi devolvido.".format(carros_alugados[codigo_carro][0]))
                    lista_carros.append(carros_alugados.pop(codigo_carro))
                    
            else: print("Escolha um veículo desta lista para devolver.")

    else: print("Digite uma opção válida.")
        
    print("\nDeseja continuar?")
    print("1 - Sim | 2 - Não")
    if (int(input()) == 2): break