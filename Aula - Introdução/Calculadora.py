import os


def operacao(num1, num2, operador):
    if (operador == "+"):
        return num1 + num2
    if (operador == "-"):
        return num1 - num2
    if (operador == "*"):
        return num1 * num2
    if (operador == "/" and num2 != 0):
        return num1 / num2
    elif (num2 == 0): return "Indivisível por 0."
    
repetir = 1

while (repetir == 1):
    os.system("cls")

    print("Digite o primeiro número: ")
    num1 = float(input())

    print("Digite a operação que deseja realizar.")
    print("Utilize os seguintes operadores:")
    print('+ (Soma), - (Subtração), * (Multiplicação), / (Divisão)')
    operador = input()

    while operador not in ["+", "-", "*", "/"]:
        print("Digite um operador válido.")
        print('" + " (Soma), " - " (Subtração), " * " (Multiplicação), " / " (Divisão)')
        operador = input()

    print("Digite o segundo número: ")
    num2 = float(input())

    print("O resultado da operação é: {}".format(operacao(num1, num2, operador)))

    print("Deseja realizar mais alguma operação?")
    print("1 - Sim, 2 - Não")
    repetir = int(input())