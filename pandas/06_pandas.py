# Databricks notebook source
df_produto = spark.table("silver_olist.products").toPandas()
df_order_items = spark.table("silver_olist.order_items").toPandas()
df_sellers = spark.table("silver_olist.sellers").toPandas()

# COMMAND ----------

df_join = df_order_items.merge(df_produto, how='left', on='idProduct')

# df_order_items.merge(df_produto, how='left', left_on='idProduct', right_on='idProduct')

# COMMAND ----------

# DBTITLE 1,Funciona mas não é bonito
df_join_1 = df_order_items.merge(df_produto, how='left', on='idProduct')
df_join_2 = df_join_1.merge(df_sellers, how='left', on='idSeller')

df_result = df_join_2.rename(columns = {"nrZipPrefix": "nrZipPrefixSeller",
                                        "descCity":"descCitySeller",
                                        "descState": "descStateSeller" })

df_result

# COMMAND ----------

df_result = (df_order_items.merge(df_produto, how='left', on='idProduct')
                           .merge(df_sellers, how='left', on='idSeller')
                           .rename(columns = {"nrZipPrefix": "nrZipPrefixSeller",
                                              "descCity":"descCitySeller",
                                              "descState": "descStateSeller" }))

df_result.head()

# COMMAND ----------

# DBTITLE 1,Group By
df_result = (df_order_items.merge(df_produto, how='left', on='idProduct')
                           .merge(df_sellers, how='left', on='idSeller')
                           .rename(columns = {"nrZipPrefix": "nrZipPrefixSeller",
                                              "descCity":"descCitySeller",
                                              "descState": "descStateSeller" }))

(df_result.groupby(by=["descCategoryName"])[['idOrder']]   # Agrupa por descCategoryName, fazendo calculo em ['idOrder']
          .count()                                         # Realiza a contagem de ['idOrder']
          .reset_index()                                   # transforma descCategoryName em coluna no resultado
          .rename(columns={"idOrder":"qtIdOrder"}))        # Renomeia o idOrder para qtIdOrder

# COMMAND ----------

df_result = (df_order_items.merge(df_produto, how='left', on='idProduct')
                           .merge(df_sellers, how='left', on='idSeller')
                           .rename(columns = {"nrZipPrefix": "nrZipPrefixSeller",
                                              "descCity":"descCitySeller",
                                              "descState": "descStateSeller" }))

df_new = (df_result.groupby(by=["descCategoryName"])[['idOrder', 'idSeller']]   # Agrupa por descCategoryName, fazendo calculo em ['idOrder']
                  .describe()                                                   # Realiza a contagem de ['idOrder']
                  .reset_index()                                               # transforma descCategoryName em coluna no resultado
                  .rename(columns={"idOrder":"qtIdOrder"}))                    # Renomeia o idOrder para qtIdOrder

columns = ['descCategoryName',"idOrdercount","idOrderunique","idOrdertop","idOrderfreq","idSellercount","idSellerunique","idSellertop","idSellerfreq"]
df_new.columns = columns
df_new.head()

# COMMAND ----------

df_result = (df_order_items.merge(df_produto, how='left', on='idProduct')
                           .merge(df_sellers, how='left', on='idSeller')
                           .rename(columns = {"nrZipPrefix": "nrZipPrefixSeller",
                                              "descCity":"descCitySeller",
                                              "descState": "descStateSeller" }))

df_new = (df_result.groupby(by=["descCategoryName"])[['idOrder', 'idSeller']]  # Agrupa por descCategoryName, fazendo calculo em ['idOrder']
                  .agg( {"idOrder": ['count'],
                         "idSeller": 'nunique'})                               # Realiza a contagem de ['idOrder']
                  .reset_index())
df_new

# COMMAND ----------

df_new = (df_order_items.merge(df_produto, how='left', on='idProduct')
                        .merge(df_sellers, how='left', on='idSeller')
                        .rename(columns = {"nrZipPrefix": "nrZipPrefixSeller",
                                          "descCity":"descCitySeller",
                                          "descState": "descStateSeller" })
                        .groupby(by=["descCategoryName"])[['idOrder', 'idSeller']]
                        .agg( {"idOrder": ['count'],
                              "idSeller": 'nunique'})
                        .reset_index())

df_new

# COMMAND ----------

df_new = (df_order_items.merge(df_produto, how='left', on='idProduct')
                        .merge(df_sellers, how='left', on='idSeller')
                        .rename(columns = {"nrZipPrefix": "nrZipPrefixSeller",
                                          "descCity":"descCitySeller",
                                          "descState": "descStateSeller" })
                        .groupby(by=["descCategoryName", 'descStateSeller'])[['idOrder', 'idSeller']]
                        .agg( {"idOrder": 'count',
                              "idSeller": 'nunique'})
                        .reset_index())

df_pivot_pedido = df_new.pivot_table(values="idOrder", columns="descStateSeller", index="descCategoryName").fillna(0)

df_pivot_sellers = (df_new.pivot_table(values="idSeller", columns='descStateSeller', index='descCategoryName')
                          .fillna(0)
                          .astype(int))
df_pivot_sellers
