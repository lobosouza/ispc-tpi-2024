import random

def generar_operacion():
    operaciones = ['+', '-', '*', '/']
    operacion = random.choice(operaciones)
    num1 = round(random.uniform(1, 10), 2)
    num2 = round(random.uniform(1, 10), 2)
    
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2
    
    return num1, operacion, num2, round(resultado, 2)

def verificar_captcha(respuesta, resultado_correcto):
    return round(float(respuesta), 2) == resultado_correcto

def main():
    num1, operacion, num2, resultado_correcto = generar_operacion()
    print(f"Resuelve la siguiente operación: {num1} {operacion} {num2} = ?")
    respuesta = input("Tu respuesta: ")
    
    if verificar_captcha(respuesta, resultado_correcto):
        print("¡Felicidades, Registro finalizado!")
    else:
        print("Respuesta incorrecta. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
