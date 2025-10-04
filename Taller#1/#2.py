#2.Contador de vocales: Escribe una función que reciba una cadena y devuelva cuántas vocales hay en total usando una lista de comparación.
vocales = ["a","e","i","o","u"]
contador = [0,0,0,0,0]
cadena = "Hola mundo"
#codigo para contar
for pos, vocal in enumerate(vocales):
  if vocal in cadena:
    for letra in cadena:
      if letra == vocal:
        contador[pos]+=1
#codigo para mostras
for pos, vocal in enumerate(vocales):
  if vocal in cadena:
    print(f"{vocal} = {contador[pos]}")
