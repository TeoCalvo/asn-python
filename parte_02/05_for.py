import time

meu_nome = "Téo Calvo"

meus_dados = [30, "Calvo", "Nah", ['Sofia', "Elaine"]]

# %%

palavra = 'banana'

for v in palavra:
    print(v)

# %%

numeros = [1,2,3,4,5,6]

for i in numeros:
    print(i**2)

# %%

for i in range(1,11):
    print(i)

# %%

for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é impar")
    
    if i == 9:
        break
else:
    print("Acabou o range!")

# %%

import datetime

init = datetime.datetime.now()

x = []
for i in range(1,10000001):
    if i % 3 != 0:
        x.append(i**2)

end = datetime.datetime.now()
print(end-init)

# %%
init = datetime.datetime.now()
x = [ i**2 for i in range(1,10000001) if i % 3 != 0 ]
end = datetime.datetime.now()
print(end-init)

# %%
