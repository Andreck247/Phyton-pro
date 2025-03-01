import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
contrasena = int(input("Introduce la longitud de la contraseña:"))
contrasena_c = ""

for i in range(contrasena):
    contrasena_c += random.choice(caracteres)
print(contrasena_c)
