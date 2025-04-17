from .validaciones import validar_decimal

#Funcion para convertir de decimal a binario

def decimal_binario(cadena):
    decimal = validar_decimal(cadena)
    binario = bin(decimal)[2:]
    return binario