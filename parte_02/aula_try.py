def le_numero():
    try:
        numero = int(input("Entre com um número: "))
        return numero

    except ValueError as err:
        print("Entre com a porra de um número válido em formato numeral (1,2,3,4...), por favorzinho.")

def impar_par(x):
    if x % 2 == 0:
        print(f"{x} é par")
    else:
        print(f"{x} é ímpar")

def main():
    numero = None
    while numero is None:
        numero = le_numero()

    impar_par(numero)

if __name__ == "__main__":
    main()