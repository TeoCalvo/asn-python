# Escreva um programa que receba o nome e a idade de uma pessoa. Depois exiba a mensagem:
# “Olá fulano, bom saber que você tem x anos. Seja bem vindo!”

nome = input("Entre com o seu nome: ")
idade = input("Entre com a sua idade: ")

msg = f"Olá {nome}, bom saber que você tem {idade} anos. Seja bem vindo!"
print(msg)

# Maneira antiga
# msg = "Olá {nome}, bom saber que você tem {idade} anos. Seja bem vindo!"
# msg = msg.format(nome=nome, idade=idade)