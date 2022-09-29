# %%

import pandas as pd

# %%

minha_series = [30, 27, 25, 54, 42]
minha_series = pd.Series(minha_series)

# %%
minha_series.mean()

# %%
minha_series.median()

# %%
minha_series.describe()

# %%
minha_series

# %%
minha_series.index
# %%
minha_series[0]

#%%
minha_series.index = list('abcde')

# %%
minha_series['a']

# %%
minha_series.loc['a']

# %%
minha_series.iloc[0]

# %%
minha_series_2 = 2 + minha_series * 10
minha_series_2
