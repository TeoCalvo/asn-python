# Criando um album de figurinhas

# %%

import random
import matplotlib.pyplot as plt

# import random as rd
# from random import randint # importa um único objeto
# from random import *       # não é comum, mas acontece

# %%

def compra_pacote(N=670, n=5):
    pacote = set([random.randint(1,N) for i in range(n)])
    return pacote

def preenche_album(N=670, n=5):
    album = set()
    count = 0
    while len(album) < N:
        pacote = compra_pacote(N, n)
        album.update(pacote)
        count += 1
    
    return count

N = 670
n = 5

ite = 10000

pacotinhos=[preenche_album(N, n) for i in range(ite)]
pacotinhos
# %%

plt.hist(pacotinhos)
plt.grid(True)
plt.title("Pacotes para completar album")
plt.show()