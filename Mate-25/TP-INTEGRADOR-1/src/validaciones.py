

# Aca se hacen la validacion de los datos ingresados por el usuario
# y se definen las funciones que se utilizan para validar los datos
# y los tipos de datos que se ingresan por teclado



# Validación de entrada para la conversión binario a decimal 

def validar_binario(cadena):
    cadena = cadena.strip()

    if not cadena:
        raise ValueError("No se ingresó ningún valor")

    if not all(caracter in "01" for caracter in cadena):
        raise ValueError("Debe ser un número binario")

    numero = int(cadena, 2)

    if cadena.lstrip("0") != cadena and numero != 0:
        raise ValueError("El número no debe tener ceros a la izquierda")

    return numero




# Validación de entrada para la conversión decimal a binario
def validar_decimal(cadena):
    cadena = cadena.strip()

    if not cadena:
        raise ValueError("No se ingresó ningún valor")

    if not cadena.isdigit():
        raise ValueError("Debe ser un número entero positivo")

    numero = int(cadena)

    if numero < 0:
        raise ValueError("El número debe ser mayor o igual a cero")

    if cadena.lstrip("0") != cadena and numero != 0:
        raise ValueError("El número no debe tener ceros a la izquierda")

    return numero