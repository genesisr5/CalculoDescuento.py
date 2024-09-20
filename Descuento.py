# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a una compra.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (10% por defecto).
    :return: El monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Programa principal

# Llamada 1: Usar el descuento predeterminado del 10%
monto_total_1 = 1500
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1
print(f"Monto total: ${monto_total_1}, Descuento aplicado: ${descuento_1}, Monto final: ${monto_final_1}")

# Llamada 2: Proporcionar un descuento del 15%
monto_total_2 = 2500
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - descuento_2
print(f"Monto total: ${monto_total_2}, Descuento aplicado: ${descuento_2}, Monto final: ${monto_final_2}")
