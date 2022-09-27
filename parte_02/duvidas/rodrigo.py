
valores = 1,2,3,4,5,32,43,2,412,23,4512,5

query = '''

SELECT * 
FROM TB_FODASE

WHERE cpf in {valores}

'''

print(query.format(valores=valores))

con = Databricks()
con.execute(query)