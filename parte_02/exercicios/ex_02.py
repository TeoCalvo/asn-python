# Faça um programa que receba o nome e a idade de uma pessoa. 

# Caso essa pessoa tenha menos de 18 anos, exiba o aviso:
# 	“Fulano, você não pode dirigir nem beber”

# Para as pessoas entre 18 e 65 anos, exiba o aviso:
# 	“FulanoFulano, bebida liberada! Só não vale dirigir!”

# Para as pessoas com mais de 65 anos, exiba o aviso:
# 	“Fulano, beba com muita moderação!”

nome = input("Entre com o seu nome: ")
idade = int(input("Entre com a sua idade: "))

if idade < 18:
    txt = f"{nome}, você não pode dirigir nem beber"
    print(txt)

elif idade <= 65:
    txt = f"{nome}, bebida liberada! Só não vale dirigir!"
    print(txt)

else:
    txt = f"{nome}, beba com muita moderação! E não misture com medicamentos."
    print(txt)