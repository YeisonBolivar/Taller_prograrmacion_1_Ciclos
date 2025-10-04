#7.Reemplazo múltiple: Dada una lista de palabras y una cadena, reemplaza todas las palabras de la lista que aparezcan en la cadena por asteriscos.
texto = "El perro seguia a un gato"
palabras_a_censurar = ["perro","gato"]

lista_palabras = texto.split()

for censura in palabras_a_censurar:
  if censura in lista_palabras:
    for index, palabra in enumerate(lista_palabras):
      if censura == palabra:
        lista_palabras[index]="*"*len(palabra)
texto_final = " ".join(lista_palabras)
print(texto)
print(texto_final)
