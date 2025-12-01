# Creamos una variable en llamada inventario para que nos guarde los productos dentro de ella 
#Aqui es donde se va a guardar el inventario del usuario
inventory = []
#Se llama la varialbe de importar csv para que podamos usar el csv donde guardaremos todos los
#datos del usuario cuando este lo necesite y asi mismo los cargaremos
import csv
#creamos una funcion llamada guardar csv donde crearemos todo el codigo para que el usuario
#guarde todos sus productos y mas adelante los pueda cargar
def save_csv():
#añadimos un condicional que nos lea el inventario y si al momento de leer leerlo no encuentra
#Ningun valor le haremos saber al usuario que el inventario esta vacio usando return 
#Para que mande la instruccion a la consola
    if len(inventory) == 0:
        print("El inventario esta vacio no tienes nada para guardar")
        return
#Usamos un bloque de Try para cubir cualquier tipo de error que se le pueda presentar al 
#Usuario dentro de este sin que lo saque del programa
    try:
#Usamos el open para que facilite la apertura del archivo y asi mismo la cerrada de este
#Adentro le asignamos donde queremos que se guarden los datos del usuario y que "w" los escriba dentro del csv
#asginamos una variable llamada newline="" para que nos ignore espacios en blanco dentro del archivo
#y le decimos que se guarde comoa archivo
        with open("inventory.csv", "w", newline='') as arichivo:
#asignamos una nueva variable llamada write donde llamaremos el tipo de archivo
#En este caso un DictWriter para que guarde numeros y nombres y sea mas facil 
#la gestion de este
            write = csv.DictWriter(arichivo, fieldnames=["Nombre", "Precio", "Cantidad", "TOTAL"])
#Usamos el writeheader para que nos cree los encabezados del csv y asi mismo
#Usamos writerows para que nos escriba todas las filas que el usuario tenga dentro del inventario
            write.writeheader()
            write.writerows(inventory)
        print("Inventario guardado con éxito en inventory.csv.")
#Usamos except para cubrir cualquier tipo de error que se le pueda presentar al usuario
#El programa no se caera y nos dira que hubo un error, este except significa que si ocurre un error de tipo IOError
#Nos dira que verifiquemos los permisos de escritura del archivo
    except IOError:
        print("Error. Verifique los permisos de escritura del archivo.")
#Usamos otro except para cubrir cualquier otro tipo de error que se le pueda presentar al usuario
#lo guardara en una variable llamada e y nos dira que ocurrio un error inesperado al guardar
    except Exception as e:
        print(f"Ocurrió un error inesperado al guardar: {e}")
#Creamos una funcion llamada cargar csv para que el usuario pueda cargar su inventario
#cuando el lo necesite
def load_csv():
    try:
#hacemos lo mismo que en la funcion guardar csv pero esta vez en vez de "w" usaremos "r" para que
#leaiga los datos que el usuario ya habia guardado
        with open("inventory.csv", "r", newline="") as archivo:
#asignamos una variable llamada reader donde llamaremos al csv.DictReader para que lea los datos
            reader = csv.DictReader(archivo)
#usamos un clear para que nos limpie el inventario y no duplique los datos
            inventory.clear()
#usamos un for para que nos lea cada fila del reader y asi mismo convierta los datos
#de string a float o int dependiendo del dato que sea y asi mismo los vaya agregando
#al inventario asignandole las Keys correspondientes
            for fila in reader:
                fila["Precio"] = float(fila["Precio"])
                fila["Cantidad"] = int(fila["Cantidad"])
                fila["TOTAL"] = float(fila["TOTAL"])
                inventory.append(fila)
            print(f"Inventario cargado. Total de productos: {len(inventory)}")
#usamos except para cubrir cualquier tipo de error que se le pueda presentar al usuario
#usamos FileNotFoundError para cubrir el error en caso de que el archivo no se encuentre
    except FileNotFoundError:
        print("El archivo no se ha encontrado.")
#usamos otro except para cubrir cualquier tipo de error de lectura o formato en el archivo csv
#en caso de que el archivo tenga un formato incorrecto
    except:
        print("Error de lectura/formato en el archivo CSV.")
#creamos una funcion llamada add product para que el usuario pueda agregar productos
def add_product():
#dentro de la funcion pedimos los datos del producto al usuario, precio, cantidad
#y los guardamos en variables correspondientes
     product_name = input("Ingresa el nombre de tu producto: ")
     price = float(input("Ingresa el precio de tu prodcuto: "))
     amount = int(input("Ingresa la cantidad de productos: "))
#creamos una variable llamada total cost para que nos calcule el costo total
#multiplicando la cantidad por el precio
     total_cost = amount*price
#usamos return para que nos devuelva un diccionario con los datos del producto
     return{
          "Nombre": product_name,
          "Precio": price,
          "Cantidad": amount,
          "TOTAL":total_cost}
#creamos una funcion llamada show inventory para que el usuario pueda ver
#todos los productos que ha guardado en el inventario
def show_inventory():
     print("=====INVENTARIO ACTUAL=====")
#Usamos un for para que nos recorra todo el inventario y nos muestre
#los productos que el usuario ha guardado
     for show_inventory in inventory:
#creamos un print para que nos muestre los datos de cada producto
          print(f"Producto: ", show_inventory["Nombre"], "Precio: ", show_inventory["Precio"], "Cantidad", show_inventory["Cantidad"], "TOTAL: ", show_inventory["TOTAL"])
#creamos una funcion llamada search products para que el usuario pueda buscar
#un producto en especifico dentro del inventario
def search_products(data):
    search_inventory = input("Digita el nombre del producto que quieres buscar en la lista: ")
#Usamos un for para que nos recorra todo el inventario y busque
#el producto que el usuario digito
    for product in data:
#Usamos un condicional para que compare el producto que el usuario digito
#con los productos que hay en el inventario y si lo encuentra se imprima en consola
        if product["Nombre"].lower() == search_inventory.lower():
            print(f"Se ha encontrado el producto en el inventario y es: {product}",)
            break
#si no lo encuentra le haremos saber al usuario que el producto no se encontro
    else: 
        print("Producto no encontrado vuelva a digitar su producto correctamente.")
#creamos una funcion llamada update products para que el usuario pueda actualizar
#los productos que ya tiene guardados en el inventario
def update_products(data):
    update = input(" Ingrese el producto que deseas actualizar: ")
#asignamos una variable llamada find en False para que nos ayude a encontrar
#el producto que el usuario desea actualizar
#en caso de que no lo encuentre le haremos saber al usuario que no se encontro el producto
    find = False
#Usamos un for para que nos recorra todo el inventario y busque
#el producto que el usuario digito
    for product in data:
        if product ["Nombre"].lower() == update.lower():
            print(" ¿que datos desea cambiar? ")
            print(" 1. nombre ")
            print(" 2. precio ")
            print(" 3. cantidad")
        
            opcion_update = int(input(" elige una opcion (1/3): "))
#usamos un condicional para que dependiendo de la opcion que el usuario elija
#se actualice el dato correspondiente
#y se añada al inventario
            if opcion_update == 1:
                nuevo_product = input(" ingrese el nuevo producto: ")
                product["Nombre"] = nuevo_product
            elif opcion_update == 2:
                nuevo_product = float(input(" ingrese el precio nuevo: "))
                product["Precio"] = nuevo_product
            elif opcion_update == 3:
                nuevo_product = int(input("Ingrese una cantidad: "))
                product["Cantidad"] = nuevo_product
                product["TOTAL"] = product["Precio"] * product["Cantidad"]            
                print("Actualizacion realizada con exito.")
            else: 
                print("No hay datos que actualizar.")
            break
        else: 
            print("Producto no encontrado. VUelve a digitarlo")
#creamos una funcion llamada delete products para que el usuario pueda eliminar
#los productos que ya no desee tener en el inventario
def delete_products(data):
#creamos una variable llamada delete donde le pediremos al usuario
#el producto que desea eliminar
    delete = input("Ingrese el producto que desea eliminar: ")
#Usamos un for para que nos recorra todo el inventario y busque
#el producto que el usuario digito
    for product in data:
#Usamos un condicional para que compare el producto que el usuario digito
#con los productos que hay en el inventario y si lo encuentra se elimine
#y le haremos saber al usuario que el producto fue eliminado correctamente
        if product ["Nombre"].lower() == delete.lower():
            data.remove(product)
            print(f"Su producto fue eliminado correctamente: {data}")
            break
    else: 
        print("Producto no encontrado.. intente de nuevo.")
#creamos una funcion llamada calculate estadistics para que el usuario pueda ver
#las estadisticas de su inventario
def calculate_estadistics():
#creamos dos variables llamadas total value y total amount
#para que nos guarden el valor total del inventario
#y la cantidad total de items registrados
    total_value = 0
    total_amount = 0
    #Usamos una lambda para crear una funcion anonima
    #creamos una variable llamada calculate subtotal que nos ayudara a calcular el subtotal de cada producto
    calculate_subtotal = (lambda p: p["Precio"] * p["Cantidad"])
    #usamos max con una lambda para encontrar el producto mas caro y el producto con mayor stock
    most_expensive = max(inventory, key=lambda product: product["Precio"])
    #hacemos lo mismo para el producto con mayor stock
    most_stock = max(inventory, key=lambda product: product ["Cantidad"])
    print("====CALCULANDO ESTADISTICAS =====")
#Usamos un for para que nos recorra todo el inventario y nos calcule
#el valor total del inventario y la cantidad total de items registrados
    for product in inventory:
#y que se lo vaya sumando a las variables que creamos anteriormente
        total_value += product ["TOTAL"]
        total_amount += product ["Cantidad"]
        show_subtotal = calculate_subtotal(product)
        print(f"El subtotal es: {show_subtotal} de el", product["Nombre"])
#Y creamos el reportede estadisticas finales
    print("=========ESTADISTICAS FINALES==========")
    print(f"Valor total del inventario ${total_value:.2f}")
    print(f"Cantidad total de item registrados: {total_amount}")
    print(f"El producto mas caro es: {most_expensive['Nombre']} con un precio de {most_expensive['Precio']:.2f}")
    print(f"El producto con mayor stock es: {most_stock['Nombre']} con una cantidad de {most_stock['Cantidad']}")
    print("========================")
#ahora pasamos a crear el menu principal del inventario usando un while true
#para que el usuario pueda interactuar con el inventario sin que el programa se caiga
while True:
#abrimos un bloque de Try para cubrir cualquier tipo de error que se le pueda presentar al 
#Usuario dentro de este sin que lo saque del programa si no ingresa numeros
        try:
            print("========BIENVENIDO AL INVENTARIO EXITO========")
            print("======MENU PRINCIPAL========")
            print("1. Agregar producto")
            print("2. Mostrar productos")
            print("3. Buscar productos")
            print("4. Actualizar productos")
            print("5. Eliminar productos")
            print("6. Estadísticas")
            print("7. Guardar CSV")
            print("8. Cargar CSV")
            print("9. Salir")
#pedimos al usuario que seleccione una opcion del menu
            option = int(input("Seleccione una opcion: "))
#usamos un condicional para que dependiendo de la opcion que el usuario elija
#se ejecute la funcion correspondiente
            if option <1 or option >9:
                print("Ingrese un numero que este entre el menu")
#en caso de que el usuario ingrese un numero fuera del rango del menu
#le haremos saber que ingrese un numero valido y usaremos continue para que
#el programa no se caiga y vuelva al menu principal
                continue
#usamos if elif para cada opcion del menu llamando a la funcion correspondiente en cada una
            if option == 1:
                #usamos una variable llamada new product para que nos guarde el producto que el usuario agregue
                #usando el apend para que lo agregue al inventario
                new_product = add_product()
                inventory.append(new_product)
                print(f"El producto guardado es: {new_product}")
#hacemos elif para cada una de las opciones del menu solamente llamando a la funcion correspondiente
            elif option == 2:
            #usamos un condicional para que nos verifique si el inventario tiene productos
            #si los tiene llamara a la funcion show inventory
            #si no tiene productos le haremos saber al usuario que el inventario esta vacio 
            #y haremos uso de return para que mande la instruccion a la consola
            # asi mismo hacemos lo mismo en cada uno hasta la opcion 6
                if inventory:
                    show = show_inventory()
                else:
                    print("==========INVENTARIO VACIO=========")
            elif option == 3:
                search_products(inventory)
            elif option == 4:
                if inventory:
                    show = update_products(inventory)
                else:
                    print("=====NO HAY NADA PARA MOSTRAR=====")
            elif option == 5:
                if inventory:
                    show = delete_products(inventory)
                else: 
                    print("===== NO HAY NADA QUE BORRAR =====")
            elif option == 6:
                    if inventory:
                        calculate_estadistics()
                    else:
                        print("===========INVENTARIO VACIO==========")
#llamamos a la funcion guardar csv y cargar csv en las opciones 7 y 8
            elif option == 7:
                    save_csv()
            elif option == 8: 
                    load_csv()
#y finalmente en la opcion 9 salimos del inventario
#usando un condicional para que nos imprima un mensaje de salida y rompa el ciclo
            elif option == 9:
                print("======= SALIENDO INVENTARIO EXITO =======")
                break
#usamos el except para cubrir cualquier tipo de error que se le pueda presentar al usuario
        except ValueError:
             print("Ingrese un dato valido porfavor.")
