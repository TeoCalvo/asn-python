# Databricks notebook source
print("Olá Mundo!")

# COMMAND ----------

print("Olá, meu nome é Téo!")

# COMMAND ----------

# DBTITLE 1,Variáveis
nome = "Lara"
print(nome) # Exibe coisas na tela

# COMMAND ----------

type(nome) # Retorna o tipo do objeto

# COMMAND ----------

nome = dbutils.widgets.text("age", "How old are you?")
