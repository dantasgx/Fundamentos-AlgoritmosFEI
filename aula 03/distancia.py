distancia = float(input("Qual distância você pretende percorrer (em km)?? "))

if distancia <= 200:
    preco = 0.5 * distancia
else:
    preco = 0.45 * distancia

print("O preço da passagem será de: R$ %.2f " % preco)