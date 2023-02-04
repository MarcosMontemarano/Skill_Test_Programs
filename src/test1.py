"""
Definir una función max() que tome como argumento dos números
y devuelva el mayor de ellos. (No utilizar la funcion max propia de
Python)

Return max value between 2 numbers
Previously, check that both parameters are int
---
Parameters

a = integer , b = integer

return integer

"""

def funcion_alt_max(a,b):
    # Comprueba valores int
    try:
        int(a)
        int(b)
        tryinteger = True
    except ValueError:
        tryinteger = False

    if a > b:
        return a
    else:
        return b

