# %%

import pandas as pd

# %%

path = "/home/teo/Área de Trabalho/asn-python/pandas/data/order_items.csv"

df = pd.read_csv(path)

# %%
# cabeçalho de linhas

df.head(2)

# %%
# cauda/rabo do arquivo

df.tail(2)
# %%
df.shape

# %%
df.columns.tolist()

# %%
df.index

# %%
