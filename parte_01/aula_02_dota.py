# %%
import requests

# %%
url = "https://api.opendota.com/api/proMatches"
dados = requests.get(url).json()

# %%

dados

# %%
len(dados)

# %%
dados[0]["radiant_name"]

# %%

# Acessando todas as chaves do dicionário
dados[0].keys()

# %%
dados[0].values()

# %%
dados[0].items()

# %%

dados[0]["user_name"]

# %%

dados[0]["user_name"] = "Téo Calvo"
dados[0]