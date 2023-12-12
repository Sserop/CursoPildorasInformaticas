def dividir():

    try:
        op1 = float(input("Ingrese el primer número: "))
        op2 = float(input("Ingrese el segundo número: "))
        resdivision = op1/op2
        print("El resultado es {:.4}".format(resdivision))
    except ValueError:
        print("El valor ingresado no es un número")
    except ZeroDivisionError:
        print("No es posible dividir por cero")
    
    finally: # Se ejecuta salga o no bien el try
        print("Programa completado.")

dividir()
