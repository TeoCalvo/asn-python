# Databricks notebook source
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# COMMAND ----------

spark_dataframe = spark.table("silver_olist.order_items")
df = spark_dataframe.toPandas()

# COMMAND ----------

type(df)

# COMMAND ----------

df.head()

# COMMAND ----------

# DBTITLE 1,Filtro
df[ df['vlPrice'] > 100 ]

# condicao = df['vlPrice'] > 100
# df[ condicao ]

# COMMAND ----------

# DBTITLE 1,Rename
df['log_price'] = np.log( df['vlPrice'] )

df['vlFreightLog'] = np.log( df['vlFreight']+1 )

# Método 1
# df = df.rename( columns={"log_price":"vlPriceLog"} )

df.rename( columns={"log_price":"vlPriceLog"}, inplace=True )

# COMMAND ----------

plt.hist( df['vlPrice'])
plt.grid(True)
plt.title("Histograma para Preço de Produto")
plt.xlabel("Valores de Produto")
plt.ylabel("Frequencia")
plt.show()

# COMMAND ----------

plt.hist( df['vlPriceLog'])
plt.grid(True)
plt.title("Histograma para Preço de Produto (log)")
plt.xlabel("Valores de Produto em Log")
plt.ylabel("Frequencia")
plt.legend(["Valores em log"])
plt.show()

# COMMAND ----------

plt.hist( df['vlPriceLog'], density=True, alpha=0.5, color='royalblue')
plt.hist( df['vlFreightLog'], density=True, alpha=0.5, color='tomato')
plt.grid(True)
plt.title("Histograma para Preço de Produto (log)")
plt.xlabel("Valores de Produto em Log")
plt.ylabel("Frequencia")
plt.legend(["Valores Produto em log", "Valores Frete em Log"])
plt.show()

# COMMAND ----------

df[['vlPriceLog', 'vlFreightLog']].describe()

# COMMAND ----------

df['vlTotalPrice'] = df['vlPrice'] + df['vlFreight']
df['vlTotalPriceLog'] = np.log( df['vlPrice'] + df['vlFreight'] )
df.head(4)

# COMMAND ----------

# DBTITLE 1,Sort_values + reset_index
# df = df.sort_values(by='vlTotalPrice')
# df = df.reset_index(drop=True)
# df

df = (df.sort_values(by='vlTotalPrice')  # Aqui ordenamos
        .reset_index(drop=True))         # Aqui resetamos os inidices

df.head()

# COMMAND ----------

df.dtypes

# COMMAND ----------

# DBTITLE 1,Tipagem dos dados
# | -> or      & -> and

condicao_numerico = (df.dtypes ==  'int64') | (df.dtypes ==  'float32') # uma serie booleana

var_nums = df.dtypes[condicao_numerico].index.tolist()
df[var_nums].describe()

# COMMAND ----------

# DBTITLE 1,Correlação
import seaborn as sn

correlacao = df[var_nums].corr()
sn.heatmap(correlacao)

# COMMAND ----------

# DBTITLE 1,Conversão
df['idOrderItem'] = df['idOrderItem'].astype('float')
df.dtypes

# COMMAND ----------

df = spark.table("silver_olist.products").toPandas()
df.head()

# COMMAND ----------

# DBTITLE 1,Não façamos essa desgraça
categoria = [] # uma lista vazia

for i in df['descCategoryName'].fillna(""):
    
    if 'ferramenta' in i:
        categoria.append('ferramenta')
    else:
        categoria.append(i)

df['nova_categoria'] = categoria
df

# COMMAND ----------

def nova_categoria(x, *args):
    for i in args:
        if i in x:
            return i.upper()
    return x.upper()

# COMMAND ----------

categorias_chaves = ['ferramenta', 'arte', 'casa', 'esporte']

nova_categoria('perfumaria', *categorias_chaves)

# COMMAND ----------

categorias_chaves = ['ferramenta', 'arte', 'casa', 'esporte', 'moveis', 'bebes']

df['descNewCategoryName'] = df['descCategoryName'].fillna("").apply(nova_categoria, args=categorias_chaves)
df.head(15)

# COMMAND ----------

def concat_string(row):
    return f"{row['nova_categoria']}_{row['descNewCategoryName']}"

df["descConcatCategoryName"] = df.apply(concat_string, axis=1)
df

# COMMAND ----------

df['vlLengthCm'] > df['vlWidthCm']

# COMMAND ----------

import requests


# COMMAND ----------

import pandas as pd
data = requests.get("https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json")
df = pd.DataFrame(data.json()['cand'])

df
