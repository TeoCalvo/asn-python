# Escreva um programa que exiba os números de 1 a 100.
# Caso o número seja divisível por 3, exiba “fizz” no seu lugar,
# e para múltiplos de 5 exiba “Buzz”. Caso seja divisível por ambos, exiba “FizzBuzz”.

for i in range(1, 101):
    
    txt = ""
    
    if i % 3 == 0:
        txt += "Fizz"
    if i % 5 == 0:
        txt += "Buzz"

    if txt == "":
        print(i)
    else:
        print(txt)

