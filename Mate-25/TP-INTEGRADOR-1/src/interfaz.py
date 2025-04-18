# Seleccioná la operación
# Ingresa el numero que queres convertir
# validar datos.

import validaciones

# Seleccionar la operación
print("Selecciona la operación que desees realizar")
print("A para convertir de decimal a binario")
print("B para convertir de binario a decimal.")

# Validar que las opciones ingresadas sean correctas.
# Se pide ingresar el número que se desea convertir.
try:
    opcion = input("opcion: ")
    validaciones.validar_opcion(opcion)
    if opcion in ("a", "A"):
        dec_a_bin = input("Ingresá el número decimal que queres convertir: ")
        validaciones.validar_decimal(dec_a_bin)

    if opcion in ("b", "B"):
        bin_a_dec = input("Ingresá el número binario que queres convertir: ")
        validaciones.validar_binario(bin_a_dec)
except ValueError as e:
    print(e)

