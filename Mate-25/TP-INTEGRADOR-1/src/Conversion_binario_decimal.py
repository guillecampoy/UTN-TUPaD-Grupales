# Se implementa función de conversión de binario a decimal
# Se proponen dos alternativas para el ejercicio
# El uso de la fiunción standard int()
# Como así también el uso de una combinación de funciones propias de string con bucles

# La función debe recibir un número binario como cadena de texto y devolver su valor decimal.
# La conversión se puede realizar utilizando la función int() de Python, especificando la base 2.

# Se documentan los parámetros recibidos en cada función 
# Se indica el tipo de excepción lanzado en caso de error, 
# el mismo solo se imprime por consola, permitiendo que el script se siga ejecutando

def binario_a_decimal(binario: str) -> int:
    """
    Convierte un número binario (como cadena de texto) a decimal.

    :param binario: Número binario como cadena de texto.
    :return: Valor decimal del número binario.
    :raises ValueError: Si el valor proporcionado no es un número binario válido.
    """
    try:
        # Convertir el número binario a decimal usando la función int() con base 2
        decimal = int(binario, 2)
        return decimal
    except ValueError as e:
        print(f"Excepción capturada!!! {e}")
        return None
# Implementación alternativa sin el uso de la función int(), utilizando cadenas y blucles
def binario_a_decimal_alternativo(binario: str) -> int:
    """
    Convierte un número binario (como cadena de texto) a decimal sin usar la función int().

    :param binario: Número binario como cadena de texto.
    :return: Valor decimal del número binario.
    :raises ValueError: Si el valor proporcionado no es un número binario válido.
    """
    try:
        decimal = 0
        longitud = len(binario)

        for i in range(longitud):
            # Obtener el dígito binario en la posición actual
            digito = int(binario[longitud - 1 - i])
            # Verificar si el dígito es válido (0 o 1)
            if digito not in (0, 1):
                raise ValueError(f"El valor '{binario}' no es un número binario válido!!!")
            # Calcular su valor decimal y sumarlo al total
            decimal += digito * (2 ** i)

        return decimal
    except ValueError as e:
        print(f"Excepción capturada!!! {e}")
        return None