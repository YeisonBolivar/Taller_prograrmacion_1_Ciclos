5.Detector de palíndromos: Crea una función que reciba una cadena y determine si es un palíndromo, ignorando espacios y mayúsculas.
texto = "ana"
texto_sin_espacio = ""
texto_invertido = ""
for letra in texto:
  if letra != " ":
    texto_sin_espacio+=letra

for letra in texto_sin_espacio:
  texto_invertido=letra+texto_invertido

if texto_sin_espacio.lower() == texto_invertido.lower():
  print(f"{texto} es palindromo")
else:
  print(f"{texto} NO es palindromo")
