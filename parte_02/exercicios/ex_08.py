# Faça um programa que receba um número e retorne seu fatorial.


def fat(x):
    res = 1
    for i in range(2,x+1):
        res *= i
    return res


numero = int(input("Entre com um número: "))

fatorial = fat(numero)

print(f"{numero}! = {fatorial}")