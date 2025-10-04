#10.Codificador por desplazamiento: Dada una cadena, crea una nueva lista donde cada letra se desplace 3 posiciones en la tabla ASCII.
texto = "un gato casi se come a gon"
lista_palabras = texto.split()
texto_codificado  = ""
for palabra in lista_palabras:
  codificado = ""
  for letra in palabra:
    codificado+=chr(ord(letra)+3)
  texto_codificado+=codificado+" "
print(texto_codificado)
