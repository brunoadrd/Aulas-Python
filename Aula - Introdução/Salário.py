print("Qual seu salário-hora?")
salario = float(input())

print("Quantas horas você trabalha no mês?")
horas_trabalhadas = float(input())

salario_bruto = salario * horas_trabalhadas

print("Salário Bruto: {:.2f}".format(salario_bruto))

print("Contribução sindical (5%): {:.2f}".format(salario_bruto * 0.05))

salario_liquido = salario_bruto - (salario_bruto * 0.05)

print("Base INSS (8%): {:.2f} - Desconto: {:.2f}".format(salario_liquido, salario_liquido * 0.08))

salario_liquido = salario_liquido - (salario_liquido * 0.08)

print("Base do Imposto de Renda (11%): {:.2f} - Desconto: {:.2f}".format(salario_liquido, salario_liquido * 0.11))

salario_liquido = salario_liquido - (salario_liquido * 0.11)

print("Salário Líquido: {:.2f}".format(salario_liquido))