import requests

respuesta = requests.get("https://digimon-api.vercel.app/api/digimon")

lista = respuesta.json()

# print("----------------")
# print("Primer Digimon: ")
# print("----------------")
# print("Nombre: " + lista[0]["name"])
# print("Level: " + lista[0]["level"])
# print("----------------")

print("----------------")
print("Digimons Champions: ")
print("----------------")
contador = 0
for digimon in lista:
    if digimon["level"] == "Champion":
        contador += 1
        print("Nombre: " + digimon["name"])
        if contador == 3:
            break
        
print("----------------")
print("Digimons Rookie: ")
print("----------------")
contador = 0
i = 1
while i < len(lista):
    if lista[i]["level"] == "Rookie":
        print("Rookie: " + lista[i]["name"])
        contador += 1
        if contador == 3:
            break
    i += 1

def mostrar_imagen(ruta):
    import urllib.request
    urllib.request.urlretrieve(ruta,"icemon.jpg")
    import climage
    screen = climage.convert("icemon.jpg", is_unicode=True)
    print(screen)

print("----------------")
print("Busca de Icemon: ")
print("----------------")
for digimon in lista:
    if digimon["name"] == "Icemon":
        print("Nombre: " + digimon["name"])
        print("Level: " + digimon["level"])
        mostrar_imagen(digimon["img"])
        break
""" 
print("----------------")
print("Busca de Digimons: ")
print("----------------")
nombre = input("Ingrese nombre del Digimon a buscar: ")
for digimon in lista:
    if digimon["name"] == nombre:
        print("Nombre: " + digimon["name"])
        print("Level: " + digimon["level"])
        break
"""