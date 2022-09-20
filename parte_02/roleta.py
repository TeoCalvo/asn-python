def pega_numero(intervalo=[1,15]):
    a,b, *_ = intervalo
    texto = f"Escolha seu número da sorte [{a}; {b}] : "
    numero = input(texto)
    numero = int(numero)
    return numero

roleta = 10
numero_sorte = pega_numero([1,10])

if roleta == numero_sorte:
    print("Você acertou!!")

elif numero_sorte > roleta:
    print("Você Errou!! Tente um número menor!")

else:
    print("Você Errou!! Tente um número maior!")