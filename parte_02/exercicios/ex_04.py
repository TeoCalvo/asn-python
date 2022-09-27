# Faça um programa que receba um número.
# Verifique se este número é primo ou não e retorne o resultado:

# 	O número x é primo
# ou
# 	O número x não é primo


def eh_primo(x=5):
    for i in range(2,x):
    
        if x % i == 0:
            return False
    
    return True


numero = int(input("Entre com um número: "))

if eh_primo(numero):
    print(f"O número {numero} é primo")
else:
    print(f"O número {numero} não é primo")