p = ["yoshi","mario","princesa"]
vidas = [10,5,3]
vida_soma= 0
for vida in vidas:
    vida_soma += vida
    vida_media = vida_soma / len(vidas)
print(vida_media)

for posicao in range(0, len(vidas)):
    if vidas[posicao] > vida_media:
        print(f"personagem: {p[posicao]}")