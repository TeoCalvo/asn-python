# Faça um programa que receba um número em segundos, converta esse número para horas, minuto e segundos. Exemplos:

# Entrada: 556
# Saída: 0:9:16

# Entrada: 140153
# Saída: 38:55:53

segundos = int(input("Entre com o número de segundos: "))

horas = segundos // (60*60)   # inteira parte, quantas horas cabem em x segundos
segundos = segundos % (60*60) # resto da divisão, quantos segundos sobram depois de contar as horas

minutos = segundos // (60)   # inteira parte, quantos minutos cabem em x segundos
segundos = segundos % (60)   # resto da divisão, quantos segundos sobram depois de contar os minutos

texto = f"{horas:0>2}:{minutos:0>2}:{segundos:0>2}"
print(texto)

