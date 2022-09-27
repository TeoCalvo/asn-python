# Faça um programa que receba 4 notas de um aluno.
# Retorne a média dessas notas, a menor e a maior nota:

# Média: x
# Menor: y
# Maior: z

notas = []                                          # Cria uma lista vazia
for i in range(1,5):                                # laço com 4 iterações (1 até o 4)
    nota = float(input(f"Entre com a nota {i}: "))  # recebe a i-ésima nota e converte p/ float
    notas.append(nota)                              # adiciona ao final da lista de notas

media = sum(notas) / len(notas)
menor = min(notas)
maior = max(notas)

print("Média:", media)
print("Menor:", menor)
print("Maior:", maior)