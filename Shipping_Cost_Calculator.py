# Calculadora de Costos de Envío (Shipping Cost Calculator)

# Entrada de valores de peso del paquete y tasa de envío (Package weight and shipping rate inputs)
weight = float(input("Enter the Package Weight in Kilograms: "))
rate = float(input("Enter the Shipping Rate per Kilogram: "))

# Calculando el costo de envío (Calculating Shipping Cost)
shipping_cost = weight * rate

# Mostrando el resultado (Display the result)
print(f"Shipping Cost: {shipping_cost} USD")
