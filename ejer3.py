#Escribir una función que calcule el área de un círculo 
# y otra que calcule el volumen de un 
# cilindro usando la primera función.

def area_circulo(radio):
    pi= 3.1416
    return pi*radio**2

def cilindro_volumen(radio,altura):
    return area_circulo(radio)*altura
    
    
print(cilindro_volumen(3,5))
