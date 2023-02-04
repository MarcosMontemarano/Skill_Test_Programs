"""
Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

"""

def davuelta(cadena):
    largo = -(len(cadena)-1)
    cadena_invertida = str()

    for n in range(largo,1):
        n = abs(n)
        cadena_invertida += cadena[n]
    
    return cadena_invertida
