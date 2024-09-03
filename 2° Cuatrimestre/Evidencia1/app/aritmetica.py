#1. La función "sumar" recibe dos números reales y devuelve la suma de los mismos
def sumar ():
    try:
        a=float(input("Ingrese el primer número de la suma: "))
        b=float(input("Ingrese el segundo número de la suma: "))
    except ValueError:
        print("Los valores ingresados deben ser números reales")
    except Exception:
        print("Algo anda mal, recuerda ingresar dos valores que sean números reales")
    
    resultado = round(a+b, 2)
    print(f'{resultado=}')
    return resultado

#2. La función "restar" recibe dos números reales y devuelve la resta del primero menos el segundo
def restar():
    try:
        a=float(input("Ingrese el primer número de la resta: "))
        b=float(input("Ingrese el segundo número de la resta: "))
    except ValueError:
        print("Los valores ingresados deben ser números reales")
    except Exception:
        print("Algo anda mal, recuerda ingresar dos valores que sean números reales")
    
    resultado = round(a-b, 2)
    print(f'{resultado=}')
    return resultado 
#3. La función "dividir" recibe dos números reales y devuelve el resultado de dividir el primer número por el segundo
def dividir():
    try:
        a=float(input("Ingrese el número del dividendo: "))
        b=float(input("Ingrese el número del divisor: "))
    except ValueError:
        print("Los valores ingresados deben ser números reales")
    except Exception:
        print("Algo anda mal, recuerda ingresar dos valores que sean números reales")

    try:
        resultado = round(a/b, 2)
        print(f'{resultado=}')
        return resultado 
    
    except ZeroDivisionError:
        print("El divisor no puede ser 0")
    except TypeError:
        print("Los valores ingresados deben ser números reales")
    except Exception:
        print("Algo anda mal, recuerda ingresar dos valores que sean números reales")

#4. La función "multiplicar" recibe dos números reales y devuelve la multiplicación de los mismos
def multiplicar():
    try:
        a=float(input("Ingrese el primer número de la multiplicación: "))
        b=float(input("Ingrese el segundo número de la multiplicación: "))
    except ValueError:
        print("Los valores ingresados deben ser números reales")
    except Exception:
        print("Algo anda mal, recuerda ingresar dos valores que sean números reales")

    resultado = round(a*b, 2)
    print(f'{resultado=}')
    return resultado 

#5. La función "sumar_n" recibe una cantidad variable (n) de números reales y devuelve la suma de los mismos
def sumar_n():

    try:
        n=[]
        while True:
            valor_n = input("Ingrese un número a sumar (para finalizar sólo presione ENTER):")
            if valor_n:
                n.append(float(valor_n))
            else:
                break
    
        print(f'{n=}')

        resultado = round(sum(n), 2)
        print(f'{resultado=}')
        return resultado 
    
    except ValueError:
        print("Los valores ingresados deben ser números reales")
    except Exception:
        print("Algo anda mal, recuerda ingresar números reales")

#6. La función "promedio_n" recibe una cantidad variable (n) de números reales y devuelve el valor promedio de los mismos
def promedio_n():

    try:
        n=[]
        while True:
            valor_n = input("Ingrese un número a promediar (para finalizar sólo presione ENTER):")
            if valor_n:
                n.append(float(valor_n))
            else:
                break
    
        print(f'{n=}')

        resultado = round(sum(n)/len(n), 2)
        print(f'{resultado=}')
        return resultado 
    
    except ValueError:
        print("Los valores ingresados deben ser números reales")
    except Exception:
        print("Algo anda mal, recuerda ingresar números reales")


#Le preguntamos al usuario qué operación aritmética desea realizar y ejeccuta la función correspondiente
while True:
    try:
        operacion = int(input("Selecciona la operación a realizar: \n 1. Suma \n 2. Resta \n 3. División \n 4. Multiplicación \n 5. Suma de dos o más elementos \n 6. Promedio de dos o más elementos"))
        if (operacion <= 6 and operacion >0):
            break
    except:
        print("Ingresá un número entero válido")

#Realizamos la operación elegida por el usuario
try:
    if operacion==1:
        sumar()
    elif operacion==2:
        restar()
    elif operacion==3:
        dividir()
    elif operacion==4:
        multiplicar()
    elif operacion==5:
        sumar_n()
    elif operacion==6:
        promedio_n()
    else:
        print("Operación no válida")
except:
    print("Operación no válida")
