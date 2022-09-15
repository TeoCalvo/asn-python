# Faça um programa que receba o raio de uma circunferência em centímetros.
# Retorne para o usuário qual é a área e perímetro desta circunferência no seguinte formato.
# Área:  x.xx
# Perímetro:  y.yy

raio = float(input("Entre com o raio da circunferencia: "))

pi = 3.14

area = round(pi * raio * raio, 2)
perimetro = round(2 * pi * raio, 2)

print("Área:", area)
print("Perímetro:", perimetro)