#4.Inversor de palabras: Dada una cadena con varias palabras, invierte el orden de las palabras usando listas.
texto = "un gato casi se come a gon"
palabra_reverse = ""
lista_palabras = []
palabra = ""
for letra in texto:
  if letra != " ":
    palabra+=letra
  else:
    lista_palabras.append(palabra)
    palabra=""
if palabra:
  lista_palabras.append(palabra)

lista_palabras_inversas = []
aux = ""
for index, final in enumerate(range(len(lista_palabras),len(lista_palabras)//2,-1)):
  aux = lista_palabras[index]
  lista_palabras[index] = lista_palabras[final-1]
  lista_palabras[final-1] = aux
print(texto)
print(lista_palabras)

