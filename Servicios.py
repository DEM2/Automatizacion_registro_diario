from collections import defaultdict

def registrar_ventas (registro, producto, precio, cantidad):
    registro.append({
        'Producto': producto,
        'Precio_unitario': precio,
        'Cantidad': cantidad
    })
    print("\n Registros Exitoso ✅")


def calculos_totales(registro):
    resumen= defaultdict(lambda: {'unidades_vendidas': 0, 'total': 0})
    for venta in registro:
        producto = venta['Producto']

        resumen[producto]['unidades_vendidas']+=venta['Cantidad']
        resumen[producto]['total']+=venta['Precio_unitario']*venta['Cantidad']
        
    return resumen

def resumen_diario (resumen):
    print("="*30)
    print("\n RESUMEN DE VENTAS DEL DÍA")
    total=0
    for producto, info in resumen.items():
        print(f"\n Producto: {producto}")
        print(f" Cantidad total vendida: {info['unidades_vendidas']}")
        total+=info['total']
    print(f"\n Total recaudado: ${total}")
    