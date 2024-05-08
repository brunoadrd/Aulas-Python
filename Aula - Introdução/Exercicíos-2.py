def aprovado(nota1, nota2):
    media = (nota1 + nota2)/2

    if (media == 10):
        print("Aluno Aprovado com Distinção!")
    elif (media >= 7):
        print("Aluno Aprovado!")
    elif (media < 7):
        print("Aluno Reprovado!")
    else: print("Algum erro ocorreu, verifique os parâmetros.")

#aprovado(7, 6)
#aprovado(10, 10)
#aprovado(7, 9)

def maiormenor(num1, num2, num3):
    numeros = sorted([num1, num2, num3])

    print("O maior número é o {} enquanto o menor é o {}".format(numeros[2], numeros[0]))

#maiormenor(3, 9, 5)

def escada(palavra):
    for i in range(len(palavra)+1): print("{}".format(palavra[0:i]))

#escada("Macaco")

def info(nome, idade, salario, sexo, estadocivil):
    
    nomevalido = len(nome) > 3
    if nomevalido: print("Nome é válido.")
    else: print("Nome é inválido.")
    
    idadevalido = 0 < idade < 150
    if idadevalido: print("Idade é válida.")
    else: print("Idade é inválida.")

    salariovalido = salario > 0
    if salariovalido: print("Salário é válido.")
    else: print("Salário é inválido.")

    sexovalido = (sexo in ["f", "m"])
    if sexovalido: print("Orientação sexual é válida.")
    else: print("Orientação sexual é inválida.")

    estadocivilvalido = (estadocivil in ["s", "c", "v", "d"])
    if estadocivilvalido: print("Estado civíl é válido.")
    else: print("Estado civíl é inválido.")

#info("Bruno", 24, 1500, "m", "s")
def validaprimo(num):
    primo = True
    
    for i in range(2, num):
        if (num % i == 0):
            print("O número não é primo")
            primo = False
            break 
        
    if (primo): print("O número é primo!")

validaprimo(3)
validaprimo(11)
validaprimo(7)
validaprimo(22)