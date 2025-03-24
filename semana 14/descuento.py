def calcular_descuento(monto_total, porcentaje_descuento=10):  #Declaro mi funcion y coloco parametros

    monto_final = monto_total - (monto_total * porcentaje_descuento / 100)   #Realizo la operacion del descuento
    return monto_final  #Retorno mi resultado

# Pedir al usuario que ingrese datos
monto_total = float(input("Ingrese el monto total de la compra: "))
num_productos = int(input("Ingrese el número de productos: "))

# Calcular el monto total después del descuento
monto_final = calcular_descuento(monto_total * num_productos)

# Mostrar los resultados
print(f"\nNúmero de productos: {num_productos}")
print(f"Monto total de la compra antes del descuento: ${monto_total * num_productos:.2f}")
print(f"Monto total después del descuento aplicado (10%): ${monto_final:.2f}")