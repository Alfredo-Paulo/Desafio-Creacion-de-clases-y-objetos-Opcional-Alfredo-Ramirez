from te import Te

# Crear instancias
te_negro = Te()
te_verde = Te()

# Almacenar tipos de datos
tipo_te_negro = type(te_negro)
tipo_te_verde = type(te_verde)

# Mostrar tipos de datos almacenados
print("Tipo de te_negro:", tipo_te_negro)
print("Tipo de te_verde:", tipo_te_verde)

# Comparar tipos de datos
if tipo_te_negro == tipo_te_verde:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")
