print("-----------------------")
print("1. Login")
print("2. Registrar usuario")
print("-----------------------")

opc = int(input("Ingrese una opcion: "))

if opc <1 or opc>2:
    print("Opción incorrecta. Ingrese nuevamente")

elif opc == 1:
    import f_login
    f_login.login()

elif opc == 2:
    import f_registro #nombre ficticio. se debe ajustar despues del desarrollo de la funcion registrar usuario
    f_registro.registro()
