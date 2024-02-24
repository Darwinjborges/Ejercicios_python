import getpass
from string import ascii_lowercase

password = getpass.getpass("Ingrese la contraseña: ")

abecedario = ascii_lowercase

cont = 0

for letra in password.lower():
    for caracter in abecedario:
        cont += 1
        if letra ==  caracter:
            break

print(f"La contraseña {password} fue forzada en {cont} intentos")
