# Considere a seguinte lista: [123, 435, 987, 1984, 2, 19, 423, -178, 320]

# Faça um programa que retorne a posição do menor e do maior valor encontrado:

# O maior valor está na posição x
# O menor valor está na posição y

x = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

maior_valor = max(x)
menor_valor = min(x)

maior_index = x.index(maior_valor)
menor_index = x.index(menor_valor)
print(x)
print(f"O maior valor está na posição {maior_index}")
print(f"O menor valor está na posição {menor_index}")