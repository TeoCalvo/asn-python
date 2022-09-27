# %%

import requests
import pandas as pd

def get_pro_players():
    url = "https://api.opendota.com/api/proPlayers"
    resposta = requests.get(url).json()

# %%

data = get_pro_players()
df = pd.DataFrame(data)
# %%

df.to_csv("dados_dota.csv", index=False)
# %%
