#%%

valores = []

# %%

valores = [30, 32, 0.999, 35]
sum(valores) / len(valores)

# %%

dados_teo = ["Teodoro",
             30,
             "Head of Data",
            ["Maria", "Marcela", "Josefina"]]

dados_teo[3][-1][0]

# %%

dados_teo.append("UNESP - Estatística")
dados_teo
# %%

dados_teo.append(["VW Fox", "Maria"])
dados_teo
# %%
dados_teo.remove(["VW Fox", "Maria"])
dados_teo
# %%
dados_teo.extend(["VW Fox", "Maria"])
dados_teo

# %%

dados_teo += ["Gamers Club", "Natalia"]
# dados_teo = dados_teo + ["Gamers Club", "Natalia"]
dados_teo

# %%

print([1,2,3] + [4,5,6])
print("FO" + "DA")

# %%

dados_teo[:2] + dados_teo[-2:]


# %%
