#9.Clasificador de palabras: Dada una cadena, clasifica las palabras en una lista según su longitud: cortas (1–3), medias (4–6), largas (7+).
texto = "un gato casi se come a gon"
lista_palabras = texto.split()
corta = []
media = []
larga = []

for palabra in lista_palabras:
  if len(palabra)<4:
    corta.append(palabra)
  elif len(palabra)<8:
    media.append(palabra)
  else:
    larga.append(palabra)
print("Palabra cortas")
if corta:
  for palabra in corta:
    print(palabra)
else:
  print("No hay palabras de tamaño corto")
print()
print("Palabra medias")
if media:
  for palabra in media:
    print(palabra)
else:
  print("No hay palabras de tamaño medio")
print()
print("Palabra largas")
if larga:
  for palabra in larga:
    print(palabra)
else:
  print("No hay palabras de tamaño largo")
print()
