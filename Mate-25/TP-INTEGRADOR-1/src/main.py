# Seleccioná la operación
# Ingresa el numero que queres convertir
# validar datos.

import validaciones
import Conversion_binario_decimal
import convertidor

# Seleccionar la operación
print("------------------------------------------")
print("TP INTEGRADOR 1: CONVERSOR BINARIO/DECIMAL")
print("------------------------------------------ \n")
print("Selecciona la operación que desees realizar")
print(" --> A para convertir de decimal a binario")
print(" --> B para convertir de binario a decimal.")

# Validar que las opciones ingresadas sean correctas.
# Se pide ingresar el número que se desea convertir.
try:
    opcion = input("opcion: ")
    validaciones.validar_opcion(opcion)
    if opcion in ("a", "A"):
        dec_a_bin = input("Ingresá el número decimal que queres convertir: ")
        validaciones.validar_decimal(dec_a_bin)
        valor_bin = convertidor.decimal_binario(dec_a_bin)
        print(f"El número decimal {dec_a_bin} convertido a binario es: {valor_bin}")

    if opcion in ("b", "B"):
        bin_a_dec = input("Ingresá el número binario que queres convertir: ")
        validaciones.validar_binario(bin_a_dec)
        valor_dec = Conversion_binario_decimal.binario_a_decimal_alternativo(bin_a_dec)
        print(f"El número binario {bin_a_dec} convertido a decimal es: {valor_dec}") 
except ValueError as e:
    print(e)

