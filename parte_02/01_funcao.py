# %%

def f(x): # assinatura da função
    # corpo da função
    resultado = 2 * (x ** 2) - 6 * x + 125
    return resultado

print( f(1) )

# %%

def g(x=0):
    return 2 * x + 10

print(g(-1))

# %%

def concat(nome, sobrenome=""):
    return f"{nome} {sobrenome}".title()

print(concat("teo"))

# %%

def concat(nome, sobrenome=""):
    '''
Essa função concatena um nome com um sobrenome, utilizando um espaço entre as palavras.
Os argumentos necessários para essa função, são:
    nome: string
    sobrenome: string
    '''
    return f"{nome} {sobrenome}".title()

print(concat("teo"))

# %%

def fodase():
    ''' Docstring
    Essa função é foda-se
    '''
    print("Foda-se")

fodase()

# %%

def concat(nome:str, sobrenome="")->str:
    '''
Essa função concatena um nome com um sobrenome, utilizando um espaço entre as palavras.
Os argumentos necessários para essa função, são:
    nome: string
    sobrenome: string
    '''
    return f"{nome} {sobrenome}"

print(concat("teo"))

# %%

def operacao(a, *args, opcao="soma"):

    if opcao == "soma":
        values = [a] + list(args) 
        return sum(values)
    
    elif opcao == "media":
        values = [a] + list(args) 
        return sum(values) / len(values)

operacao(10, 1,2,3,4,5,6,7,8, opcao="media")

# %%

def config( teclado, mouse, **kwargs ):
    print("Teclado:", teclado)
    print("Mouse:", mouse)
    print(kwargs)

config("Logitech", "Logitech", headset="Corsair", monitor="LG")

# %%

query = '''
select {fodase}
from {tb_nao_sei}
where date > {date}
'''

def format_query(query:str, **kwargs):
    res =  query.format(**kwargs)
    return res

query_format = format_query(query,
                            fodase="teste",
                            tb_nao_sei="fodase",
                            date="'2022-09-19'")

print(query_format)