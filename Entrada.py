entrada=input()
print(type(entrada))
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero)
#definimos si en caso es entero 
    print("DATO ENTERO. MUY BIEN")
else:
    #y si no agregamos como else para dirigir print
    print("Dato no es entero. Intentar nuevamente")
