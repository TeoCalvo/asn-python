# %%

notas = [1.5, 2.7] # notas
n1, n2 = notas

print("n1 =",n1)
# %%

notas = [1.5, 2.7, 7.6, 8.4] # notas
*_, n1, n2 = notas

print("n1 =",n1)
print("n2 =",n2)
print("_ =",_)

# %%

notas = [1.5, 2.7, 7.6, 8.4] # notas
n1, *_, n2 = notas

print("n1 =",n1)
print("n2 =",n2)
print("_ =",_)

# %%

a = 10
b = 20

c = a
a = b
b = c
print("a =", a)
print("b =", b)

# %%

a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

# %%

letras = 'abcdefghijklmnopqrstuvxz'
letras = list(letras)

a,b, *fodase  = letras

print(letras)