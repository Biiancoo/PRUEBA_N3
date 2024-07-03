import os,time,csv
compras=[]
compras_puentealto=[]
compras_laflorida=[]
compras_lapintana=[]

def validar_opciones(opciones):
    
    while True:
        try:
            opc = int(input("Ingrese una opcion: "))
            if opc in opciones:
                return opc
            else:
                print("ERROR, debe ingresar una copcion permitida")


        except:
            print("ERROR,debe ingresar la opcion en valor nummerico")


def registrar_pedido():

    os.system("cls")
    print("REGISTRAR PEDIDO")
    while True:
        try:
            rut = int(input("Ingrese RUT del comprador sin guion ni digito verificador\n(si el rut termina en K replacelo con un 0): "))
            if rut >99999999 and rut<999999999 :
                print("Rut guardado")
                time.sleep(2)
                break
            else:
                print("El rut ingresado no es valido!")
        except:
            print("El rut debe ser ingresado solo con numeros")

    while True:
        os.system("cls")
        try:
            nombre = str(input("Ingrese nombre del comprador: "))
            if nombre.strip and len(nombre)>=3 and len(nombre) <24:
                print("Nombre guiardado con éxito!")
                time.sleep(2)
                break
            else:
                print("ERROR,debe ingresar el nombre correctamente")
        except:
            print("Debe ingrear el nombre sin numeros ni signos!")

    os.system("cls")
    direccion = input("Ingrese la dirección del comprador: ")

    while True:
        os.system("cls")
        print("COMUNAS")
        print("1. Puente Alto")
        print("2. La Florida")
        print("3. La Pintana")
        opciones = (1,2,3)
        opc = validar_opciones(opciones)
        if opc ==1:
            comuna = "Puente Alto"
            break
        elif opc ==2:
            comuna = "La Florida"
            break
        else:
            comuna = "La Pintana"
            break

    cant_cilindros_15kl=0
    cant_cilindros_5kl=0
    while True:
        os.system("cls")
        print("PEDIDO")
        print("1. Cilindro 5 kilos $12.500 pesos")
        print("2. Cilindro 15 kilos $25.500 pesos")
        cilindros=(1,2)
        opc_cilindro = validar_opciones(cilindros)
        os.system("cls")
        if opc_cilindro ==1:
            while True:
                try:
                    cant_cilindros_5kl= int(input("Ingrese cuantos desea llevar: "))
                    if cant_cilindros_5kl > 0 and cant_cilindros_5kl <101:
                        print ("Cantidad de cilindros guardada")
                        time.sleep(2)
                        print("Desearia agragar cilindros de 15 kilos?")
                        print("Valor cilindro 15 kilos = $25.500 pesos")
                        print("1. Si")
                        print("2. No")
                        agregar=(1,2)
                        continuar_compra = validar_opciones(agregar)
                        if continuar_compra == 1:
                            while True:
                                try:
                                    cant_cilindros_15kl = int(input("Ingrese cuantos desea llevar: "))
                                    if cant_cilindros_15kl > 0 and cant_cilindros_15kl <101:
                                        print ("Cantidad de cilindros guardada")
                                        time.sleep(2)
                                        break
                                    else:
                                        print("Debe ingresar una cantidad de (1-100)")
                                except:
                                    print("Debe ingresar cuandos desea llevar en valor numerico!")
                            break
                        else:
                            
                            break
                    else:
                        print("Debe ingresar una cantidad de (1-100)")
                except:
                    print("Debe ingresar cuandos desea llevar en valor numerico!")
            break
        else:
            while True:
                try:
                    cant_cilindros_15kl= int(input("Ingrese cuantos desea llevar: "))
                    if cant_cilindros_15kl > 0 and cant_cilindros_15kl <101:
                        print ("Cantidad de cilindros guardada")
                        time.sleep(2)
                        print("Desearia agragar cilindros de 5 kilos?")
                        print("Valor cilindro 5 kilos = $12.500 pesos")
                        print("1. Si")
                        print("2. No")
                        agregar=(1,2)
                        continuar_compra = validar_opciones(agregar)
                        if continuar_compra == 1:
                            while True:
                                try:
                                    cant_cilindros_5kl = int(input("Ingrese cuantos desea llevar: "))
                                    if cant_cilindros_5kl > 0 and cant_cilindros_5kl <101:
                                        print ("Cantidad de cilindros guardada")
                                        time.sleep(2)
                                        break
                                    else:
                                        print("Debe ingresar una cantidad de (1-100)")
                                except:
                                    print("Debe ingresar cuandos desea llevar en valor numerico!")
                            break
                        else:
                            
                            break
                    else:
                        print("Debe ingresar una cantidad de (1-100)")
                except:
                    print("Debe ingresar cuandos desea llevar en valor numerico!")
            break
    
    if cant_cilindros_5kl != 0 and cant_cilindros_15kl !=0 :
        total_cilindros5kl=cant_cilindros_5kl*12500
        total_cilindros15kl=cant_cilindros_15kl*25500
        total_compra= total_cilindros15kl + total_cilindros5kl
    if cant_cilindros_15kl != 0 and cant_cilindros_5kl==0:
        total_cilindros15kl=cant_cilindros_15kl*25500
        total_compra= total_cilindros15kl
    if cant_cilindros_5kl != 0 and cant_cilindros_15kl==0:
        total_cilindros5kl=cant_cilindros_5kl*12500
        total_compra= total_cilindros5kl

    datos_compras=[rut,nombre,direccion,comuna,cant_cilindros_5kl,cant_cilindros_15kl,total_compra]
    compras.append(datos_compras)
    if opc == 1:
        compras_puentealto.append(datos_compras)
    elif opc == 2:
        compras_laflorida.append(datos_compras)
    elif opc ==3:
        compras_lapintana.append(datos_compras)

    print("Datos guardados con éxito!!")
    time.sleep(3)


def listar_pedidos():
    os.system("cls")
    if not compras:
        print("No hay compras registradas")
        time.sleep(2)
    else:
        print("RUT  CLIENTE     DIRECCION   COMUNA  CIL.5KG     CIL.15KG    TOTAL")
        for compradores in compras:
            print(compradores)
        time.sleep(3)
            

def buscar_pedido():
    os.system("cls")
    buscar_rut = input("Ingrese Rut del comprador: ")
    pocicion = buscar_rut.index()

    if buscar_rut in compras:
        print(compras(pocicion))
        time.sleep(2)
    else:
        print("No hay ninguna compra con ese rut asociado")
        time.sleep(2)


def imprimir_hoja():
    os.system("cls")
    if not compras:
        print("no se puede crear el archivo por que no hay compras registradas")
        time.sleep(2)
    else:
        print("COMUNAS")
        print("1. Puente Alto")
        print("2. La Florida")
        print("3. La Pintana")
        opciones=(1,2,3)
        opc = validar_opciones(opciones)
        if opc == 1:
            try:
                nombre_archivo= input("Ingrese nombre del archivo: ")
                with open(f"{nombre_archivo}.csv","x",newline="")as archivo:
                    escritor = csv.writer(archivo)
                    escritor.writerow("Compras y datos de la gente que compro en Puente Alto")
                    for compradores in compras_puentealto:
                        escritor.writerow(compradores)
                print("Datos impimidos con éxito")
                time.sleep(2)


            except:
                print("ERROR, no puede haber dos archivos con el mismo nombre")  
                time.sleep(2)              
                
            

        elif opc ==2:
            try:
                nombre_archivo= input("Ingrese nombre del archivo: ")
                with open(f"{nombre_archivo}.csv","x",newline="")as archivo:
                    escritor = csv.writer(archivo)
                    escritor.writerow("Compras y datos de la gente que compro en La Florida")
                    for compradores in compras_laflorida:
                        escritor.writerow(compradores)
                print("Datos impimidos con éxito")
                time.sleep(2)


            except:
                print("ERROR, no puede haber dos archivos con el mismo nombre")
                time.sleep(2)

        else:
            try:
                nombre_archivo= input("Ingrese nombre del archivo: ")
                with open(f"{nombre_archivo}.csv","x",newline="")as archivo:
                    escritor = csv.writer(archivo)
                    escritor.writerow("Compras y datos de la gente que compro en La Pintana")
                    for compradores in compras_lapintana:
                        escritor.writerow(compradores)
                print("Datos impimidos con éxito")
                time.sleep(2)


            except:
                print("ERROR, no puede haber dos archivos con el mismo nombre")
                time.sleep(2)


        
    