class Te:
    # Atributos de clase que contienen los precios, tiempos de preparación y recomendaciones
    PRECIOS = {300: 3000, 500: 5000}  # Precios por formato en un diccionario
    TIEMPOS = {1: 3, 2: 5, 3: 6}  # Tiempos de preparación por sabor en un diccionario
    RECOMENDACIONES = {1: "Consumir al desayuno", 2: "Consumir al medio día", 3: "Consumir al atardecer"}  # Recomendaciones por sabor en un diccionario

    @staticmethod
    def obtener_tiempo_y_recomendacion(sabor):
        """Método estático para obtener el tiempo de preparación y la recomendación según el sabor."""
        tiempo = Te.TIEMPOS.get(sabor)
        recomendacion = Te.RECOMENDACIONES.get(sabor)
        return tiempo, recomendacion

    @staticmethod
    def obtener_precio(formato):
        """Método estático para obtener el precio según el formato."""
        return Te.PRECIOS.get(formato)

