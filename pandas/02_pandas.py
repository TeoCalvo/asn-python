# %%

import pandas as pd

# %%

df_dict = {
    "nome": ['Téo', "Nah", "Maria"],
    "idade": [30, 32, 1],
    "sexo": ["M", "F", "F"]
}

df = pd.DataFrame(df_dict)

df
# %%
df['nome']

# %%
type(df['nome'])

# %%
df.describe()

# %%
df['nome'].describe()