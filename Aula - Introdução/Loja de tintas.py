from math import ceil


print("Quantos m^2 deseja pintar?")
metragem = input()

tintapormetro = 1 / 3
pedidocliente = (float(metragem) * tintapormetro) / 18
pedidocliente = ceil(pedidocliente) * 80

print("Valor R$ {}".format(pedidocliente))