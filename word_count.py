from collections import Counter

def contar_caracteres_distintos(texto):
  caracteres = set(texto)
  return len(caracteres)

def contar_palabras_distintas(texto):
  palabras = texto.split(" ")
  palabras_sin_vacios = [palabra for palabra in palabras if palabra]
  return len(set(palabras_sin_vacios))

def main():
  with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()

  numero_caracteres_distintos = contar_caracteres_distintos(texto)
  numero_palabras_distintas = contar_palabras_distintas(texto)

  print(f"El número de caracteres distintos es: {numero_caracteres_distintos}")
  print(f"El número de palabras distintas es: {numero_palabras_distintas}")

if __name__ == "__main__":
  main()