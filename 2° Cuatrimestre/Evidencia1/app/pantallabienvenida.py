"""variables: us = nombre de usuario, pwd = contraseña. 
Estas variables serán comparadas con clave-valor en el diccionario cuando haya un registro de usuario"""

print('                   Ingrese usuario y contraseña para ingresar al sistema')
us = input("nombre de usuario ")
pwd = input("contraseña ")

user_credentials = {"usuario":{us}, "contra":{pwd}}

# print(user_credentials) verificar si se agregó al diccionario

print('Bienvenido!')
