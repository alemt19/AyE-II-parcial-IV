from datetime import datetime
import cola as co
import proyecto as pr
from tareas import Tareas

class Gestion:
    def __init__(self):
        self.proyectos = []
    
    def menu(self):
        x = 1
        while x != 0:
            print("1. Gestionar Proyectos")
            print("2. Gestionar Tareas y Prioridades")
            print("-presione 0 para salir del programa")
            x = int(input("ingrese una opcion: "))

            if x == 1:
                print("-presione 1 para crear un proyecto")
                print("-presione 2 para modificar un proyecto")
                print("-presione 3 para consultar un proyecto")
                print("-presione 4 para eliminar un proyecto")
                print("-presione 5 para listar los proyectos actuales")
                print("-presione 0 para salir del programa")
                x = int(input("ingrese una opcion: "))
                print("------------------------")
                if x == 1:
                    self.crear_proyecto()
                elif x == 2:
                    self.modificar_proyecto()
                elif x == 3:
                    self.consultar_proyecto()
                elif x == 4:
                    self.eliminar_proyecto()
                elif x == 5:
                    self.listar_proyectos()
            elif x == 2:
                id = int(input("Ingrese el id del proyecto del que se desea gestionar las tareas: "))
                proyecto = self.elegir_proyecto(id)
                print("------------------------")
                print("-presione 1 para agregar una nueva tarea")
                print("-presione 2 para insertar una nueva tarea en una posición dada")
                print("-presione 3 para modificar una tarea")
                print("-presione 4 para buscar una tarea")
                print("-presione 5 para eliminar una tarea")
                print("-presione 6 gestionar tareas prioritarias")
                print("-presione 0 para salir del programa")
                x = int(input("ingrese una opcion: "))
                print("------------------------")
                if x == 1:
                    self.agregar_tarea(proyecto)
                elif x == 2:
                    i = input(f"Inserte la posición especifica donde quiera agregar la tarea (cantidad actual de tareas: {len(proyecto.tareas)}): ")
                    self.insertar_tarea(proyecto, i)
                elif x == 3:
                    id = int(input("Ingrese el id de la tarea que desea modificar: "))
                    self.modificar_tarea(proyecto, id)
                elif x == 4:
                    self.buscar_tarea(proyecto)
                elif x == 5:
                    self.eliminar_tarea(proyecto)
                elif x == 6:
                    print("------------------------")
                    print("-presione 1 para agregar una tarea prioritaria")
                    print("-presione 2 para eliminar una tarea prioritaria")
                    print("-presione 3 para consultar la tarea con más prioridad")
                    print("-presione 4 para consultar el tiempo total de las tareas prioritarias")
                    print("-presione 0 para salir del programa")
                    x = int(input("ingrese una opcion: "))
                    print("------------------------")
                    if x == 1:
                        self.agregar_priotitaria(proyecto)
                    elif x == 2:
                        self.eliminar_prioritaria(proyecto)
                    elif x == 3:
                        self.consultar_prioritaria(proyecto)


        print("fin del programa")
    
    def crear_proyecto(self):
        nom = input("ingrese el nombre del proyecto: ")
        desc = input("ingrese la descripcion del proyecto: ")
        fi = input("ingrese la fecha de inicio en formato YYYY-MM-DD: ")
        fid = datetime.strptime(fi, "%Y-%m-%d")
        ff = input("ingrese la fecha final del proyecto en formato YYYY-MM-DD: ")
        ffd = datetime.strptime(ff, "%Y-%m-%d")
        estado = input("ingrese el estado de el proyecto: ")
        empresa = input("ingrese la empresa del proyecto: ")
        gerente = input("ingrese el gerente del proyecto: ")
        equipo = input("ingrese el equipo del proyecto: ")
        proyecto = pr.Proyecto(nom, desc, fid, ffd, estado, empresa, gerente, equipo)
        self.proyectos.append(proyecto)
        print("proyecto agregado correctamente!")
        print("---------------------------")
    
    def modificar_proyecto(self):
        m = input("ingrese el nombre del proyecto a modificar: ")
        if self.proyectos.buscar_nombre(m):
            print("-presione 1 para modificar el nombre")
            print("-presione 2 para modificar la descripcion")
            print("-presione 3 para modificar la fecha de inicio")
            print("-presione 4 para modificar la fecha de vencimiento")
            print("-presione 5 para modificar el estado")
            print("-presione 6 para modificar el gerente")
            print("-presione 7 para modificar la empresa")
            print("-presione 8 para modificar el equipo")
            xm = int(input("ingrese una opcion: "))
            print("-------------------------------")
            for i in self.proyectos:
                if m == i.nombre:
                    proyecto = i
                    break
            
            if xm == 1:
                nuevo_nombre = input("ingrese el nuevo nombre del proyecto: ")
                proyecto.nombre = nuevo_nombre
                print("proyecto modificado exitosamente!")
            elif xm == 2:
                nueva_desc = input("ingrese la nueva descripcion del proyecto: ")
                proyecto.descripcion = nueva_desc
                print("proyecto modificado exitosamente!")
            elif xm == 3:
                nueva_fi = input("ingrese la nueva fecha de inicio del proyecto en formato YYYY-MM-DD: ")
                proyecto.fecha_inicio = datetime.strptime(nueva_fi, "%Y-%m-%d")
                print("proyecto modificado exitosamente!")
            elif xm == 4:
                nueva_ff = input("ingrese la nueva fecha de vencimiento del proyecto en formato YYYY-MM-DD: ")
                proyecto.fecha_fin = datetime.strptime(nueva_ff, "%Y-%m-%d")
                print("proyecto modificado exitosamente!")
            elif xm == 5:
                nuevo_estado = input("ingrese el nuevo estado del proyecto: ")
                proyecto.estado = nuevo_estado
                print("proyecto modificado exitosamente!")
            elif xm == 6:
                nuevo_gerente = input("ingrese el nuevo gerente del proyecto: ")
                proyecto.gerente = nuevo_gerente
                print("proyecto modificado exitosamente!")
            elif xm == 7:
                nueva_empresa = input("ingrese la nueva empresa del proyecto: ")
                proyecto.empresa = nueva_empresa
                print("proyecto modificado exitosamente!")
            elif xm == 8:
                nuevo_equipo = input("ingrese el nuevo equipo del proyecto: ")
                proyecto.equipo = nuevo_equipo
                print("proyecto modificado exitosamente!")
            else:
                print("error, opcion no valida")
        else:
            print("proyecto no encontrado")
    
    def consultar_proyecto(self):
        m = input("ingrese el nombre del proyecto a consultar: ")
        print("-------------------------------")
        for proyecto in self.proyectos:
            if m==proyecto.nombre:
                print(f"id: {proyecto.id}")
                print(f"nombre: {proyecto.nombre}")
                print(f"descripcion: {proyecto.descripcion}")
                print(f"fecha de inicio: {proyecto.fecha_inicio}")
                print(f"fecha de vencimiento: {proyecto.fecha_fin}")
                print(f"estado: {proyecto.estado}")
                print(f"empresa: {proyecto.empresa}")
                print(f"gerente: {proyecto.gerente}")
                print(f"equipo: {proyecto.equipo}")
        print("------------------------------")

    def eliminar_proyecto(self):
        m = input("ingrese el nombre del proyecto a eliminar: ")
        for i in self.proyectos:
            if m == i.nombre:
                self.proyectos.pop(i)
    
    def listar_proyectos(self):
        for i in self.proyectos:
            print(f"-{i.nombre}")

    def agregar_tarea(self, proyecto):
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

    def insertar_tarea(self, proyecto, i):
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

    def modificar_tarea(self, proyecto, id):
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
        
    def buscar_tarea(self, proyecto):
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
        
    def eliminar_tarea(self, proyecto):
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

    def agregar_priotitaria(self, proyecto):
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
    
    def eliminar_prioritaria(self, proyecto):
        
        if proyecto.tareas_prioritarias.ver_tope():
            proyecto.tareas_prioritarias.eliminar()
            print("Se ha eliminado correctamente la tarea")
        else:
            print("No hay ninguna tarea marcada como prioritaria")
        
    
    def consultar_prioritaria(self, proyecto):
        if proyecto.tareas_prioritarias.ver_tope():
            tarea = proyecto.tareas_prioritarias.ver_tope()
            print(f"{tarea.nombre} {tarea.empresa} {tarea.cliente}")
        else:
            print("No hay ninguna tarea marcada como prioritaria")

    def elegir_proyecto(self, id):
        for i in self.proyectos:
            if i.id == id:
                return i