#3.Filtro de palabras cortas: Dada una lista de palabras, elimina todas las que tengan menos de 4 letras.
texto = "un gato casi se come a gon"
lista_palabras = []
palabra = ""

#codigo para separar la cadena por espacios

for letra in texto:
  if letra != " ":
    palabra+=letra
  else:
    lista_palabras.append(palabra)
    palabra=""
#este if es para que incluya la ultima interaccion del for
if palabra:
  lista_palabras.append(palabra)

lista_filtrada = []

#creo una lista auxiliar donde incluyo las palabras a eliminar
for palabra in lista_palabras:
  if len(palabra)<4:
    lista_filtrada.append(palabra)

#recorro la lista auxiliar para eliminar cada palabra en el texto
for eliminar in lista_filtrada:
  lista_palabras.remove(eliminar)

texto_final = ""

#recorro finalmente la lista de palabras para entregar el texto como cadena
for palabra in lista_palabras:
  texto_final+=palabra+" "
print("Texto: ", texto)
print("texto filtrado: ", texto_final)
