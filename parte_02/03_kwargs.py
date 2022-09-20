from re import match


def import_book(path:str, **kwargs):
    file_open = open(path, "r")
    texto = file_open.read()
    file_open.close()
    return texto.format(**kwargs)

data = {"nome":"Dani", "anos":30}

text = import_book("romance_teo.txt",**data)
print(text)

