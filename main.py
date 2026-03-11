from Servicios import registrar_ventas, resumen_diario, calculos_totales

registro_ventas = []
resumen=[]
seguir = True

while seguir != False :

    print("\n","-"*30)
    print("      Registro de Ventas")
    print("-"*30)

    Producto=input("\n Ingresar el nombre del Producto: ")
    precio=float(input("\n Ingresar el precio de la unidad: "))
    ventas=int(input(f"\n ¿Cuantas unidades de {Producto}?: "))

    registrar_ventas(registro_ventas, Producto, precio, ventas)
    opcion = input("\n Desea continuar registrando ventas, S para si o N para no: ")
    if (opcion=="N"):  seguir=False
    
resumen=calculos_totales(registro_ventas)
resumen_diario(resumen)
