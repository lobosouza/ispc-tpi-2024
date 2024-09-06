import random

from sqlalchemy import false, true

cap = False

def realizar_operacion():
    operaciones = ['+', '-', '*', '/']
    operacion = random.choice(operaciones)
    num1 = int(random.uniform(1, 10))
    num2 = int(random.uniform(1, 10))

    if operacion == '+':
        resultado = round((num1 + num2), 0)
    elif operacion == '-':
        resultado = round((num1 - num2), 0)
    elif operacion == '*':
        resultado = round((num1 * num2), 0)
    elif operacion == '/':
        resultado = round((num1 / num2), 0)

    print(f"Resuelve la siguiente operación: {num1} {operacion} {num2} = ?")
    respuesta = int(input("Tu respuesta: "))

    if respuesta == resultado:
        print("CAPTCHA CORRECTO")
        cap = True

    else:
        print("CAPTCHA INCORRECTO. Inténtalo de nuevo.")
        realizar_operacion()
        cap = False
    
