def get_valid_number(msg):
    numero = None
    while numero == None:

        numero = input(msg)
        
        try:
            numero = int(numero)
            return numero
        
        except ValueError as err:
            numero = None
            print("Entre com um número válido (1,2,3...)\n\n")


def check_number(numero_sorte, roleta):

    if roleta == numero_sorte:
        print("Você acertou!!")
        return True

    elif numero_sorte > roleta:
        print("Você Errou!! Tente um número menor!")
        return False

    else:
        print("Você Errou!! Tente um número maior!")
        return False

tentativas = 3
roleta = 10

for i in range(tentativas):
    numero_sorte = get_valid_number("Entre com um numero entre 1 e 10: ")
    check = check_number(numero_sorte, roleta)
    if check == True:
        break
    else:
        print(f"Você tem mais {tentativas-i-1} tentativas")
else:
    print("Suas tentativas abaram, entre com mais fichas!")
