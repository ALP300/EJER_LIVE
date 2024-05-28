#Escribir una función que reciba una muestra 
# de números en una lista y devuelva otra 
# lista con sus cuadrados.
def cuadrados(lista):
    listaCuadrados=[]
    for i in lista:
        listaCuadrados.append(i**2)
    return listaCuadrados



print(cuadrados([1,2,3,4,5]))