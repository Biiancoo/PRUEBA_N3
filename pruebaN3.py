from funciones_pruebaN3 import *
while True:
    os.system("cls")
    print("Gaxplosive")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Buscar pedido por RUT")
    print("4. Imprimir hoja de ruta")
    print("5. Salir del programa")
    opciones=(1,2,3,4,5)
    opc = validar_opciones(opciones)

    if opc == 1:
        registrar_pedido()
    elif opc==2:
        listar_pedidos()
    elif opc==3:
        buscar_pedido()
    elif opc==4:
        imprimir_hoja()
    else:
        print("ADIOS!!")
        break