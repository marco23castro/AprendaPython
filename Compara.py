numero1=input("Numero 1:")
numero2=input("Numero 2:")
salida="Numero proporcionados: {} y {}. {} {}."
if (numero1==numero2):
    #entra aqui si los numeros soniguales
    print(salida.format(numero1,numero2, "Los numeros son iguales"))
    else:
        #aqui es si no son iguales
        if numero1>numero2:
            #aqui si el mayor es primero
            print(salida.format(numero1,numero2, "El mayor es el primero"))
        else:
            #si no el segundo
            print(salida.format(numero1,numero2, "El mayor es el segundo"))
