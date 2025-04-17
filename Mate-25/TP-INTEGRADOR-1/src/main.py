import Conversion_binario_decimal

# Ejemplo de uso de la función binario_a_decimal
# Se proponen una serie de entradas válidas e inválidas para probar la función

# Ejemplos usando la función binario_a_decimal con uso de la función int()
print("==================================================================================")
print("Ejemplo de uso de la función binario_a_decimal (uso función int())")
print("==================================================================================")

#Entradas válidas
print("-------------------")
print("Entradas VALIDAS")
print("-------------------")

# Entrada válida 1
binario_valido1 = "1101010"
binario_convertido1 = Conversion_binario_decimal.binario_a_decimal(binario_valido1)
print(f"El número binario {binario_valido1} en decimal es: {binario_convertido1}")
print()

# Entrada válida 2
binario_valido2 = "1101010000"
binario_convertido2 = Conversion_binario_decimal.binario_a_decimal(binario_valido2)
print(f"El número binario {binario_valido2} en decimal es: {binario_convertido2}")
print()

# Entrada válida 3
binario_valido3 = "1110001101010"
binario_convertido3 = Conversion_binario_decimal.binario_a_decimal(binario_valido3)
print(f"El número binario {binario_valido3} en decimal es: {binario_convertido3}")
print()

#Entradas INVALIDAS
print("-------------------")
print("Entradas INVALIDAS")
print("-------------------")
# Entrada inválida 1
binario_invalido1 = "HOLA"
binario_invalido_convertido1 = Conversion_binario_decimal.binario_a_decimal(binario_invalido1)
print(f"El número binario {binario_invalido1} en decimal es: {binario_invalido_convertido1}")
print()

# Entrada invalida 2
binario_invalido2 = "333333"
binario_invalido_convertido2 = Conversion_binario_decimal.binario_a_decimal(binario_invalido2)
print(f"El número binario {binario_invalido2} en decimal es: {binario_invalido_convertido2}")
print()

# Entrada invalida 3
binario_invalido3 = "?78734TESTS"
binario_invalido_convertido3 = Conversion_binario_decimal.binario_a_decimal(binario_invalido3)
print(f"El número binario {binario_invalido3} en decimal es: {binario_invalido_convertido3}")
print()



print("==================================================================================")
print("Ejemplo de uso de la función binario_a_decimal_alternativo (sin uso función int())")
print("==================================================================================")
# Ejemplo de uso de la función binario_a_decimal_alternativo sin uso de la función int()
# Se proponen las MISMAS entradas para validad integridad de ambas propuestas
# Entradas válidas
print("-------------------")
print("Entradas VALIDAS")
print("-------------------")
# Entrada válida 1
binario_valido1 = "1101010"
binario_convertido1_alter = Conversion_binario_decimal.binario_a_decimal_alternativo(binario_valido1)
print(f"El número binario {binario_valido1} en decimal es: {binario_convertido1}")
print(f"Igualdad con uso de función int()", {binario_convertido1 == binario_convertido1_alter})
print()

# Entrada válida 2
binario_valido2 = "1101010000"
binario_convertido2_alter = Conversion_binario_decimal.binario_a_decimal_alternativo(binario_valido2)
print(f"El número binario {binario_valido2} en decimal es: {binario_convertido2}")
print(f"Igualdad con uso de función int()", {binario_convertido2 == binario_convertido2_alter})
print()

# Entrada válida 3
binario_valido3 = "1110001101010"
binario_convertido3_alter = Conversion_binario_decimal.binario_a_decimal_alternativo(binario_valido3)
print(f"El número binario {binario_valido3} en decimal es: {binario_convertido3}")
print(f"Igualdad con uso de función int()", {binario_convertido3 == binario_convertido3_alter})
print()

#Entradas INVALIDAS
print("-------------------")
print("Entradas INVALIDAS")
print("-------------------")
# Entrada inválida 1
binario_invalido1 = "HOLA"
binario_invalido_convertido1 = Conversion_binario_decimal.binario_a_decimal_alternativo(binario_invalido1)
print(f"El número binario {binario_invalido1} en decimal es: {binario_invalido_convertido1}")
print()

# Entrada invalida 2
binario_invalido2 = "333333"
binario_invalido_convertido2 = Conversion_binario_decimal.binario_a_decimal_alternativo(binario_invalido2)
print(f"El número binario {binario_invalido2} en decimal es: {binario_invalido_convertido2}")
print()

# Entrada invalida 3
binario_invalido3 = "?78734TESTS"
binario_invalido_convertido3 = Conversion_binario_decimal.binario_a_decimal_alternativo(binario_invalido3)
print(f"El número binario {binario_invalido3} en decimal es: {binario_invalido_convertido3}")