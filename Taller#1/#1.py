# 1.Separador de caracteres: Dada una cadena, conviértela en una lista donde cada carácter esté separado por un espacio.
cadena = "hola mundo"
lista = []
for letra in cadena:
  letra=" "+letra+" "
  lista.append(letra)
print("Lista = ",lista)
