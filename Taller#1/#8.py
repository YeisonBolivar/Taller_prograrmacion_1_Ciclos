#8.Extracción de números: Dada una cadena con texto y números mezclados, extrae todos los números y guárdalos en una lista.
cadena = "Mi casa es 123 y mi número es 4567"
numeros = ["1","2","3","4","5","6","7","8","9","0"]
numero = ""
lista_numeros = []
for i in cadena:
  if i in numeros:
    numero+=i
  else:
    if numero:
      lista_numeros.append(numero)
      numero=""
if numero:
      lista_numeros.append(numero)
      numero=""

print(lista_numeros)


