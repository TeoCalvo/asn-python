# %%

meu_nome = "Teodoro Calvo"

# %%

tamanho = len(meu_nome)
print("meu nome tem tantas letras:", tamanho)

# %%

print("Primeira letra:", meu_nome[0])
print("Segunda letra:", meu_nome[1])

print("Última letra:", meu_nome[12]) # isso e a o último index

tamanho = len(meu_nome)
print("Última letra:", meu_nome[tamanho-1])

print("Última letra:", meu_nome[-1])

print("Penúltima letra:", meu_nome[-2])

# %%

# Fatimento

print(meu_nome[0:3]) # meu_nome[start:stop] range=stop-start

print(meu_nome[8:11]) # Fatiamento no meio

print(meu_nome[0:-1]) # Todos menos a última letra

print(meu_nome[:3]) # As três primeiras

print(meu_nome[-3:]) # As três última

# %%
# Step

print(meu_nome[::2]) # Pula de 2 em 2

# meu_nome[start:stop:step]
print(meu_nome[:3:2]) # Pula de 2 em 2

print(meu_nome[::-1]) # Inverte a ordem da string
