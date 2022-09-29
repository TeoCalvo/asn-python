# %%

import pandas as pd

# %%

path = "/home/teo/Área de Trabalho/asn-python/pandas/data/order_items.csv"
df = pd.read_csv(path)

df.head()

# %%

df.info(memory_usage='deep')
# %%

df.dtypes
# %%
df.describe()

# %%
df.columns.tolist()

# %%
df['vlPrice'][0] ## df[coluns][index]

# %%

prices = ['vlPrice', 'vlFreight']
df[prices]

df[['vlPrice', 'vlFreight']]
# %%

df[['vlPrice']]

# %%
df.head()

# %%
# Acessando a linha do dataframe pelo índice
df.loc[3]

# %%
# Acessando a linha do dataframe pela ordem da linha
df.iloc[3]

# %%

s_price = df['vlPrice'].sort_values()
s_price.loc[3]
# %%
s_price.iloc[3]
# %%

bool_menor_1 =  df['vlPrice'] < 1
bool_menor_1

df[bool_menor_1]

# %%

df_fodase = pd.DataFrame({
    "nome": ["Téo", 'Nah', "Maria"],
    "idade": [30,32, 1],
    "sexo":["M", "F", "F"],
    "peso": [312,54,35342],
    "altura":[312,421,4512]
})

bool_fodase = df_fodase['sexo'] == 'F'
bool_fodase

# %%
df_fodase[bool_fodase]

# %%
df_fodase[['peso', 'altura']] % 2 == 0

# %%
condicao = df_fodase['peso'] > df_fodase['altura']
df_fodase[condicao]

# %%
condicao = (df_fodase['idade'] % 2 == 0) & (df_fodase['sexo']=='F')
df_fodase[condicao]

# %%
df_mulheres = df_fodase[df_fodase['sexo']=='F'].copy()
df_mulheres['nota'] = [10,9.5]

# %%
df_mulheres['idade'] = df_mulheres['idade'] + 10
df_mulheres

# %%

A = [1,2,3]
B = A.copy()

B[2] = 'Téo'

print("B:", B)
print("A:", A)