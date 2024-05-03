from te import Te

# Función para obtener la entrada del usuario
def obtener_valor(mensaje, tipo):
    """Función para obtener un valor del usuario, asegurándose de que sea del tipo especificado."""
    while True:
        try:
            valor = tipo(input(mensaje))
            break
        except ValueError:
            print("Por favor, ingrese un valor válido.")
    return valor

# Obtener datos del pedido
sabor = obtener_valor("Ingrese el sabor (1:Té negro, 2:Té verde, 3:Agua de hierbas): ", int)
formato = obtener_valor("Ingrese el formato (300 o 500 gr): ", int)

# Crear instancia de Te
te = Te()

# Obtener tiempo, recomendación y precio
tiempo, recomendacion = te.obtener_tiempo_y_recomendacion(sabor)
precio = te.obtener_precio(formato)

# Mostrar detalle del pedido
if sabor == 1:
    nombre_sabor = "Té negro"
elif sabor == 2:
    nombre_sabor = "Té verde"
else:
    nombre_sabor = "Agua de hierbas"

print("Detalle del pedido:")
print("Sabor:", nombre_sabor)
print("Formato:", formato, "gr")
print("Precio: $", precio)
print("Tiempo de preparación:", tiempo, "minutos")
print("Recomendación:", recomendacion)
