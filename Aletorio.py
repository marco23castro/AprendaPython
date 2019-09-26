import random
numero1=float(10.5)
#al elegir una variable float le damos un valor cualquiera
def mifuncion():
#aqui se convierte a float el numero que dirigimos en la plantilla o columna anterior 
    numero2=float(random.randrange(1,10))
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))
    mifuncion()
