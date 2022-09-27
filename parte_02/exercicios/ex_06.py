# Faça um programa com uma função que recebe uma frase.
# Para cada palavra nesta frase, inverta a ordem das letras.
# Exiba o resultado:

# 	Esta é a frase original

# 	atsE é a esarf lanigiro

# %%

frase = "Esta é a frase original"

frase_lista = frase.split()

frase_nova = ""
for palavra in frase_lista:
    frase_nova = frase_nova + palavra[::-1] + " "

print(frase_nova)


# %%

frase_nova = " ".join([palavra[::-1] for palavra in frase.split(sep=" ")])
print(frase_nova)

# %%
