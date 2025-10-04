#6.Frecuencia de letras: Dada una cadena, crea un diccionario que cuente cuántas veces aparece cada letra.

abecedario = [chr(x) for x in range(ord("a"), ord("z")+1)]
texto = "Hola mundo"
texto = texto.lower()
contador = [0]*len(abecedario)
for pos,letra in enumerate(abecedario):
  if letra in texto:
    for i in texto:
      if i == letra:
        contador[pos]+=1

for pos, letra in enumerate(abecedario):
  if letra in texto:
    print(f"{letra} = {contador[pos]}")
