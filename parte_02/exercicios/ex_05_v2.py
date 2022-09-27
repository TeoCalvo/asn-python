# Faça um programa que receba um número.
# Este número corresponde à uma posição na sequência de Fibonacci: 0, 1, 1, 2, 3, 5,...

# Exiba o número da sequência cuja posição foi informada:
# A posição x corresponde ao número y

def fib(pos):
    
    fib_seq = [0,1]
    
    while True:

        try:
            return fib_seq[pos]
        
        except IndexError:
            fib_seq.append(fib_seq[-1]+fib_seq[-2])

numero = int(input("Entre com uma posição da Seq Fib: "))
print(fib(numero))