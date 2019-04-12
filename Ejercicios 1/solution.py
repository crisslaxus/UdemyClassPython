#librerias
import math

#E9
total_compra = float(input("Total de COMPRA: "))
descuento = (15 * total_compra)/100
total_pago = total_compra - descuento
print("Total a pagar: {0}".format(total_pago))