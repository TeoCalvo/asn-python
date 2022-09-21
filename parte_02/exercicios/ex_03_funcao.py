# Faça um programa que receba um número.
# Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira:

# 	O número x é impar
# ou
# 	O número x é par

numero1 = int(input("Entre com um número: "))
numero2 = int(input("Entre com um número: "))

def check_par(x:int):
    '''Funcao que calcula se o número é par ou impar.
    É necessário que se passe um valor INTEIRO
    
    Será retornado um valor booleano (True=par, False=ímpar)

    x:int
    '''
    if x % 2 == 0:
        print(f"{x} é par")
    else:
        print(f"{x} é impar")

check_par(numero1)
check_par(numero2)