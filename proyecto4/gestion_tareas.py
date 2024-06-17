from datetime import datetime
from tareas import Tareas

def agregar_tarea( proyecto):
    nombre = input("Ingrese el nombre de la tarea a agregar: ")
    empresa = input("Ingrese la empresa: ")
    cliente = input("Ingrese el nombre del cliente: ")
    descripcion = input("Ingrese una descripción de la tarea: ")
    fecha_de_inicio = input("Ingrese la fecha de inicio de la tarea separada por guiones: ")
    fecha_de_vencimiento = input("Ingrese la fecha de vencimiento separada por guiones: ")
    estado = "Pendiente"
    porcentaje = 0
    tarea = Tareas(nombre, empresa, cliente, descripcion, fecha_de_inicio, fecha_de_vencimiento, estado, porcentaje)
    proyecto.tareas.append(tarea)

def insertar_tarea( proyecto, i):
    nombre = input("Ingrese el nombre de la tarea a agregar: ")
    empresa = input("Ingrese la empresa: ")
    cliente = input("Ingrese el nombre del cliente: ")
    descripcion = input("Ingrese una descripción de la tarea: ")
    fecha_de_inicio = input("Ingrese la fecha de inicio de la tarea separada por guiones: ")
    fecha_de_vencimiento = input("Ingrese la fecha de vencimiento separada por guiones: ")
    estado = "Pendiente"
    porcentaje = 0
    tarea = Tareas(nombre, empresa, cliente, descripcion, fecha_de_inicio, fecha_de_vencimiento, estado, porcentaje)
    proyecto.tareas.insert(i, tarea)

def modificar_tarea(proyecto, id):
    tarea = proyecto.tareas[id]
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
        nueva_empresa = input("ingrese el nuevo cliente de la tarea: ")
        tarea.empresa = nueva_empresa
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
        tarea.equipo = nuevo_porcentaje
        print("Tarea modificada exitosamente!")
    else:
        print("error, opcion no valida")
        
def buscar_tarea (proyecto):
    print("Presione 1 para buscar tareas por nombre")
    print("Presione 2 para buscar tareas por empresa")
    print("Presione 3 para buscar tareas por cliente")
    x = int(input("Ingrese un numero: "))
    tareas = []
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
    if len(tareas) == 0:
        print("No se encontraron tareas con el criterio dado")
    else:
        print("Se encontraron las siguientes tareas: \n")
        for i in tareas:
            print(f"{i.nombre}")
        
def eliminar_tarea( proyecto):
    nombre = input("Ingrese el nombre de la tarea que se desea eliminar: ")
    n = 0
    for i in proyecto.tareas:
        if nombre == i.nombre:
            proyecto.tareas.pop(n)
            n = -1
            break
        n = n + 1
    if n == -1:
        print("Se ha eliminado correctamente la tarea")
    else:
        print("No se ha encontrado una tarea con el nombre dado")

def agregar_priotitaria(proyecto):
    nombre = input("Ingrese el nombre de la tarea que se desea agregar: ")
    n = 0
    for i in proyecto.tareas:
        if nombre == i.nombre:
            proyecto.tareas_prioritarias.agregar(i)
            n = -1
            break
        n = n + 1
    if n == -1:
        print("Se ha agregado correctamente la tarea")
    else:
        print("No se ha encontrado una tarea con el nombre dado")
    
def eliminar_prioritaria(proyecto):
        
    if proyecto.tareas_prioritarias.ver_tope():
        proyecto.tareas_prioritarias.eliminar()
        print("Se ha eliminado correctamente la tarea")
    else:
        print("No hay ninguna tarea marcada como prioritaria")
        
    
def consultar_prioritaria(proyecto):
    if proyecto.tareas_prioritarias.ver_tope():
        tarea = proyecto.tareas_prioritarias.ver_tope()
        print(f"{tarea.nombre} {tarea.empresa} {tarea.cliente}")
    else:
        print("No hay ninguna tarea marcada como prioritaria")

def agregar_tarea_venc(proyecto):
    nombre = input("Ingrese el nombre de la tarea que se desea agregar: ")
    n = 0
    lista_temp = []
    for i in proyecto.tareas:
        if nombre == i.nombre:
            while proyecto.tareas_proximas_avencer:
                if i.fecha_fin < proyecto.tareas_proximas_avencer.ver_frente():
                    proyecto.tareas_proximas_avencer.agregar(i)
                    break
                elif proyecto.tareas_proximas_avencer.fin.siguiente is not None and proyecto.tareas_proximas_avencer.esta_vacia():
                    if i.fecha_fin < proyecto.tareas_proximas_avencer.ver_frente():
                        proyecto.tareas_proximas_avencer.agregar(i)
                        break
                    else:
                        temp = proyecto.tareas_proximas_avencer.eliminar_frente()
                        proyecto.tareas_proximas_avencer.agregar(i)
                        proyecto.tareas_proximas_avencer.agregar(temp)
                        break
                else:
                    lista_temp.append(proyecto.tareas_proximas_avencer.eliminar_frente())
            n = -1
            break
        n = n + 1

    for i in lista_temp:
        proyecto.tareas_proximas_avencer.agregar(i)

    if n == -1:
        print("Se ha agregado correctamente la tarea")
    else:
        print("No se ha encontrado una tarea con el nombre dado")

def eliminar_tarea_venc(proyecto):
    if proyecto.tareas_proximas_avencer.esta_vacia():
        print("No hay tareas agregadas a la lista de próximas a vencer")
    else:
        proyecto.tareas_proximas_avencer.eliminar_frente()

def consultar_tarea_venc(proyecto):
    if proyecto.tareas_proximas_avencer.esta_vacia():
        print("No hay tareas agregadas a la lista de próximas a vencer")
    else:
        tarea = proyecto.tareas_proximas_avencer.ver_frente()
        print(f"{tarea.nombre} {tarea.fecha_fin}")

def elegir_proyecto(proyectos, id):
    for i in proyectos:
        if i.id == id:
            return i