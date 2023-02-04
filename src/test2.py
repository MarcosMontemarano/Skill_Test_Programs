"""
Escribir una función que tome un caracter y devuelva True si es una vocal,
de lo contrario devuelve False.

"""

def es_vocal(caracter):
    vocales = ['a','e','i','o','u']
    if caracter in vocales:
        return print("el caracter ingresado es una vocal")
    else:
        return print("el caracter ingresado es una consonante")

print(es_vocal("j"))
