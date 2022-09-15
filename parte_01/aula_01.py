# %%
print("Olá mundo!!")

# %%

nome = input("Entre com o seu nome: ")
print(nome)
# %%

nome = input("Entre com o seu nome: ")
print("Seu nome é:", nome)

# %%
print('Hoje não é meu dia!')

# %%

texto_longo = '''
Este é um texto bem grande

eu nem sei porque eu deveria escrever algo assim

foda-se
'''

print(texto_longo)

# %%

print("1+1 =",1+1)
print("10-231 =",10-231)
print("10*2 =", 10 * 2)
print("10 / 3 = ", 10 / 3)
print("10 % 3 = ", 10 % 3)
print("10 // 3 = ", 10 // 3)
print("10**2 = ", 10 ** 2)
print("4**(1/2) = ", 4**(1/2))

print("True =", True)
print("False =", False)
print("True + True =", True + True)

# %%

raio = 3                # definiu o raio
pi = 3.14               # definiu o valor de pi
area = pi * (raio ** 2) # calculou a área

print("Area =", area)
# %%

# Calcula média de idade entre 2 pessoas
idade_1 = input("Idade pessoa1: ")
idade_1 = int(idade_1)

idade_2 = int(input("Idade pessoa2: "))

media = (idade_1 + idade_2) / 2

print("Média:", media)