# Definir una función max() que tome como argumento dos números
# y devuelva el mayor de ellos. (No utilizar la funcion max propia de
# Python)

"""
Return max value between 2 numbers

Parameters

a = integer , b = integer

return integer

"""

def max(a,b):
    try:
        int(a)
        int(b)
        tryinteger = True
    except ValueError:
        tryinteger = False

    #if tryinteger = True
    return tryinteger  