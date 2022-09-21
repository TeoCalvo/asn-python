# %%

num = 1
while num <= 10:
    print(num)
    num += 1

print("Acabou!")

# %%

num = 1
while True:
    print("Fodase!")
    
    if num == 5:
        print("Parando o laço...")
        break
    
    num += 1

print("Parou!")
# %%

num = 0
while num <=3:

    num += 1
    print(f"Fodase! {num}")
    
    if num % 2 == 0:
        continue

    print("Isso só é para impares!!")
    
    if num == 5:
        print("Parando o laço...")
        break

else:
    print("Parou! com sucesso!")

