from datetime import datetime
from tareas import Tareas

def agregar_tarea(proyecto):
    # Funcion que pide por teclado los atributos de una nueva tarea
    # Para agregarse a un objeto Proyecto dado

    nombre = input("Ingrese el nombre de la tarea a agregar: ")
    empresa = input("Ingrese la empresa: ")
    descripcion = input("Ingrese una descripción de la tarea: ")
    fecha_de_inicio = input("Ingrese la fecha de inicio de la tarea separada por guiones: ")
    fi=datetime.strptime(fecha_de_inicio,"%Y-%m-%d")
    fecha_de_vencimiento = input("Ingrese la fecha de vencimiento separada por guiones: ")
    fv=datetime.strptime(fecha_de_vencimiento,"%Y-%m-%d")
    estado = "Pendiente"
    porcentaje = 0
    tarea = Tareas(nombre, descripcion, fi, fv, estado,empresa, porcentaje)
    proyecto.tareas.append(tarea)

def insertar_tarea(proyecto, i):
    # Funcion que inserta una nueva tarea de forma similar a la funcion anterior
    # Solo que se inserta en un indice especificado

    nombre = input("Ingrese el nombre de la tarea a agregar: ")
    empresa = input("Ingrese la empresa: ")
    descripcion = input("Ingrese una descripción de la tarea: ")
    fecha_de_inicio = input("Ingrese la fecha de inicio de la tarea separada por guiones: ")
    fi=datetime.strptime(fecha_de_inicio,"%Y-%m-%d")
    fecha_de_vencimiento = input("Ingrese la fecha de vencimiento separada por guiones: ")
    fv=datetime.strptime(fecha_de_vencimiento,"%Y-%m-%d")
    estado = "Pendiente"
    porcentaje = 0
    tarea = Tareas(nombre, descripcion, fi, fv, estado,empresa, porcentaje)
    proyecto.tareas.insert(i, tarea)

def modificar_tarea(proyecto, nombre):
    # Funcion que modifica un atributo de una tarea dada

    tarea = None
    for i in proyecto.tareas:
        # Ciclo para elegir la tarea a modificar según el nombre dado por el usuario
        if nombre == i.nombre:
            tarea = i
            break
    
    if tarea is None:
        # Se verfica si se encontró una tarea
        print("No se ha encontrado una tarea con el nombre dado")
    else:
        # Menu para modificar el atributo deseado
        # Se modifican directamente los atributos del objeto Tarea
        print("-presione 1 para modificar el nombre")
        print("-presione 2 para modificar la empresa")
        print("-presione 3 para modificar el cliente")
        print("-presione 4 para modificar la descripcion")
        print("-presione 5 para modificar la fecha de inicio")
        print("-presione 6 para modificar la fecha de vencimiento")
        print("-presione 7 para modificar el estado")
        print("-presione 8 para modificar el porcentaje")
        xm = int(input("ingrese una opcion: "))
        print("-------------------------------")
            
        if xm == 1:
            nuevo_nombre = input("ingrese el nuevo nombre de la tarea: ")
            tarea.nombre = nuevo_nombre
            print("Tarea modificada exitosamente!")
        elif xm == 2:
            nueva_empresa = input("ingrese la nueva empresa de la tarea: ")
            tarea.empresa = nueva_empresa
            print("Tarea modificada exitosamente!")
        elif xm == 3:
            nuevo_cliente = input("ingrese el nuevo cliente de la tarea: ")
            tarea.cliente = nuevo_cliente
            print("Tarea modificada exitosamente!")
        elif xm == 4:
            nueva_desc = input("ingrese la nueva descripcion de la tarea: ")
            tarea.descripcion = nueva_desc
            print("Tarea modificada exitosamente!")
        elif xm == 5:
            nueva_fi = input("ingrese la nueva fecha de inicio de la tarea en formato YYYY-MM-DD: ")
            tarea.fecha_inicio = datetime.strptime(nueva_fi, "%Y-%m-%d")
            print("Tarea modificada exitosamente!")
        elif xm == 6:
            nueva_ff = input("ingrese la nueva fecha de vencimiento de la tarea en formato YYYY-MM-DD: ")
            tarea.fecha_fin = datetime.strptime(nueva_ff, "%Y-%m-%d")
            print("Tarea modificada exitosamente!")
        elif xm == 7:
            nuevo_estado = input("ingrese el nuevo estado de la tarea: ")
            tarea.estado = nuevo_estado
            print("Tarea modificada exitosamente!")
        elif xm == 8:
            nuevo_porcentaje = int(input("ingrese el nuevo porcentaje de la tarea: "))
            tarea.porcentaje = nuevo_porcentaje
            print("Tarea modificada exitosamente!")
        else:
            print("error, opcion no valida")

        
def buscar_tarea(proyecto):
    # Funcion que busca e imprime las tareas que coincidan con el criterio deseado
    print("Presione 1 para buscar tareas por nombre")
    print("Presione 2 para buscar tareas por empresa")
    print("Presione 3 para buscar tareas por cliente")
    x = int(input("Ingrese un numero: "))
    tareas = []

    # Condicionales para tomar las tareas que coincidan con el criterio
    if x == 1:
        xm = input("Ingrese el nombre de la tarea: ")
        for i in proyecto.tareas:
            if xm == i.nombre:
                tareas.append(i)
    elif x == 2:
        xm = input("Ingrese la empresa de la tarea: ")
        for i in proyecto.tareas:
            if xm == i.empresa:
                tareas.append(i)
    elif x == 3:
        xm = input("Ingrese el cliente de la tarea: ")
        for i in proyecto.tareas:
            if xm == i.cliente:
                tareas.append(i)
        
    print("------------------")
    # Condicionales para verificar si se encontraron tareas, en ese caso se imprimen
    if len(tareas) == 0:
        print("No se encontraron tareas con el criterio dado")
    else:
        print("Se encontraron las siguientes tareas: \n")
        for i in tareas:
            print(f"{i.nombre}")
        
def eliminar_tarea(proyecto):
    # Funcion para eliminar una tarea según su nombre
    nombre = input("Ingrese el nombre de la tarea que se desea eliminar: ")
    n = 0
    for i in proyecto.tareas:
        # Ciclo para borrar la tarea si coincide con el nombre dado
        if nombre == i.nombre:
            proyecto.tareas.pop(n)
            n = -1
            break
        n = n + 1
    
    # Condicionales para verificar e informar al usuario si se eliminó la tarea
    if n == -1:
        print("Se ha eliminado correctamente la tarea")
    else:
        print("No se ha encontrado una tarea con el nombre dado")

def agregar_priotitaria(proyecto):
    # Funcion para agregar tareas prioritarias a una pila, que se almacena en un atributo de la clase Tarea
    # Para determinar la prioridad de una tarea se usa la misma logica de las pilas
    # La ultima en agregarse es la más prioritaria
    nombre = input("Ingrese el nombre de la tarea que se desea agregar: ")
    n = 0
    for i in proyecto.tareas:
        # Ciclo para agregar la tarea prioritaria a la pila si su nombre corresponde con el dado
        if nombre == i.nombre:
            proyecto.tareas_prioritarias.agregar(i)
            n = -1
            break
        n = n + 1
    
    # Se verifica si se agregó la tarea a la pila de prioritarias
    if n == -1:
        print("Se ha agregado correctamente la tarea")
    else:
        print("No se ha encontrado una tarea con el nombre dado")
    
def eliminar_prioritaria(proyecto):
    # Funcion que elimina la tarea más prioritaria
    if proyecto.tareas_prioritarias.ver_tope():
        # Si la pila no está vacía se elimina el tope
        proyecto.tareas_prioritarias.eliminar()
        print("Se ha eliminado correctamente la tarea")
    else:
        print("No hay ninguna tarea marcada como prioritaria")
        
    
def consultar_prioritaria(proyecto):
    # Funcion que imprime la tarea más prioritaria
    if proyecto.tareas_prioritarias.ver_tope():
        # Si la pila no está vacía imprime el tope
        tarea = proyecto.tareas_prioritarias.ver_tope()
        print(f"{tarea.nombre}, {tarea.descripcion}, {tarea.fecha_inicio}, {tarea.fecha_fin}, {tarea.estado}, {tarea.empresa}, {tarea.porcentaje}")
    else:
        print("No hay ninguna tarea marcada como prioritaria")

def agregar_tarea_venc(proyecto):
    # Funcion que agrega una tarea dada a una cola de tareas prox a vencer
    nombre = input("Ingrese el nombre de la tarea que se desea agregar: ")
    n = 0
    lista_temp = []
    for i in proyecto.tareas:
        # Ciclo para tomar la tarea que se quiere agregar
        if nombre == i.nombre:
            while proyecto.tareas_proximas_avencer:
                # Ciclo que evalua las siguientes condiciones para determinar la posicion de la tarea
                if proyecto.tareas_proximas_avencer.ver_frente() is None:
                    # Si la cola esta vacia la tarea se agrega
                    proyecto.tareas_proximas_avencer.agregar(i)
                    break
                   
                elif (i.fecha_fin-i.fecha_inicio) > (proyecto.tareas_proximas_avencer.ver_frente().fecha_fin-proyecto.tareas_proximas_avencer.ver_frente().fecha_inicio):
                    # Se verifica si el tope de la cola esta más proximo a vencer que la tarea a agregarse
                    proyecto.tareas_proximas_avencer.agregar(i)
                    break
                else:
                    # Si no se cumple lo anterior entonces el tope se almacena en una lista temporal
                    temp = proyecto.tareas_proximas_avencer.eliminar_frente()
                    proyecto.tareas_proximas_avencer.agregar(i)
                    proyecto.tareas_proximas_avencer.agregar(temp)
                    break
            n = -1
            break
        n = n + 1

    for i in lista_temp:
        # Se vuelven a agregar las tareas de la lista temp a la cola
        proyecto.tareas_proximas_avencer.agregar(i)

    if n == -1:
        print("Se ha agregado correctamente la tarea")
    else:
        print("No se ha encontrado una tarea con el nombre dado")

def eliminar_tarea_venc(proyecto):
    # Metodo que elimina la tarea más proxima a vencer
    if proyecto.tareas_proximas_avencer.esta_vacia():
        print("No hay tareas agregadas a la lista de próximas a vencer")
    else:
        proyecto.tareas_proximas_avencer.eliminar_frente()
        print("Se ha eliminado correctamente la tarea más proxima a vencer")

def consultar_tarea_venc(proyecto):
    # Funcion  que imprime los datos de la tarea más proxima a vencer
    if proyecto.tareas_proximas_avencer.esta_vacia():
        print("No hay tareas agregadas a la lista de próximas a vencer")
    else:
        tarea = proyecto.tareas_proximas_avencer.ver_frente()
        print(f"{tarea.nombre} {tarea.fecha_fin}")

def elegir_proyecto(proyectos, nombre):
    # Funcion para elegir un proyecto según su id
    for i in proyectos:
        if i.nombre == nombre:
            return i