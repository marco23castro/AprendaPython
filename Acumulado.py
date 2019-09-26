#se declaran las variables de trabajo con tipo explicito
acumulado=int(0)
numero=str("")
while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        #si el numero es nada pues se sale
        print("Vacio. Salida del programa.")
        break
        #terminas
    else:
        acumulado+int(numero)
        salida="Monto acumulado; {}"
        print(salida.format(acumulado))
