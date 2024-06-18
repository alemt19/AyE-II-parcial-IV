from datetime import datetime
import cola as co
import proyecto as pr
from tareas import Tareas
import gestion_tareas
import reportes

class Gestion:
    def __init__(self):
        self.proyectos = []
    
    def menu(self):
        x = 1
        while x != 0:
            print("1. Gestionar Proyectos")
            print("2. Gestionar Tareas y Prioridades")
            print("3. Reportes")
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
                nombre = input("Ingrese el nombre del proyecto del que se desea gestionar las tareas: ")
                proyecto = gestion_tareas.elegir_proyecto(self.proyectos, nombre)
                print(proyecto)
                print("------------------------")
                print("-presione 1 para agregar una nueva tarea")
                print("-presione 2 para insertar una nueva tarea en una posición dada")
                print("-presione 3 para modificar una tarea")
                print("-presione 4 para buscar una tarea")
                print("-presione 5 para eliminar una tarea")
                print("-presione 6 gestionar tareas prioritarias")
                print("-presione 7 gestionar tareas proximas a su fecha de vencimiento")
                print("-presione 0 para salir del programa")
                x = int(input("ingrese una opcion: "))
                print("------------------------")
                if x == 1:
                    gestion_tareas.agregar_tarea(proyecto)
                elif x == 2:
                    i = int(input(f"Inserte la posición especifica donde quiera agregar la tarea (cantidad actual de tareas: {len(proyecto.tareas)}): "))
                    gestion_tareas.insertar_tarea(proyecto,i)
                elif x == 3:
                    id = int(input("Ingrese el id de la tarea que desea modificar: "))
                    gestion_tareas.modificar_tarea(proyecto, id)
                elif x == 4:
                    gestion_tareas.buscar_tarea(proyecto)
                elif x == 5:
                    gestion_tareas.eliminar_tarea(proyecto)
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
                        gestion_tareas.agregar_priotitaria(proyecto)
                    elif x == 2:
                        gestion_tareas.eliminar_prioritaria(proyecto)
                    elif x == 3:
                        gestion_tareas.consultar_prioritaria(proyecto)
                elif x == 7:
                    print("------------------------")
                    print("-presione 1 para agregar una tarea cercana a su fecha de vencimiento")
                    print("-presione 2 para eliminar una tarea cercana a su fecha de vencimiento")
                    print("-presione 3 para consultar la tarea con más cercana a su fecha de vencimiento")
                    print("-presione 0 para salir del programa")
                    x = int(input("ingrese una opcion: "))
                    print("------------------------")
                    if x == 1:
                        gestion_tareas.agregar_tarea_venc(proyecto)
                    elif x == 2:
                        gestion_tareas.eliminar_tarea_venc(proyecto)
                    elif x == 3:
                        gestion_tareas.consultar_tarea_venc(proyecto)
            elif x == 3:
                print("------------------------")
                print("-presione 1 consultar tareas por estado")
                print("-presione 2 para filtrar tareas por fecha")
                print("-presione 3 para filtrar proyectos")
                print("-presione 4 para listar subtareas de un proyecto")
                print("-presione 0 para salir del programa")
                x = int(input("ingrese una opcion: "))
                print("------------------------")

                if x == 1:
                    nombre = input("Ingrese el nombre del proyecto del que se desea filtrar las tareas: ")
                    proyecto = gestion_tareas.elegir_proyecto(self.proyectos, nombre)
                    estado = input("Ingrese el estado de las tareas que se desean filtrar: ")
                    reportes.consultar_tareas_estado(proyecto,estado)
                elif x == 2:
                    nombre = input("Ingrese el nombre del proyecto del que se desea gestionar las tareas: ")
                    proyecto = gestion_tareas.elegir_proyecto(self.proyectos, nombre)
                    reportes.filtrado_por_fecha(proyecto)
                elif x == 3:
                    reportes.consultar_proyectos(self.proyectos)
                elif x == 4:
                    nombre = input("Ingrese el nombre del proyecto del que se desea listar las tareas: ")
                    proyecto = gestion_tareas.elegir_proyecto(self.proyectos, nombre)
                    reportes.listar_subtareas(proyecto)


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
        band=0
        print("-------------------------------")
        for proyecto in self.proyectos:
            if m.lower()==proyecto.nombre.lower():
                print(f"id: {proyecto.id}")
                print(f"nombre: {proyecto.nombre}")
                print(f"descripcion: {proyecto.descripcion}")
                print(f"fecha de inicio: {proyecto.fecha_inicio}")
                print(f"fecha de vencimiento: {proyecto.fecha_fin}")
                print(f"estado: {proyecto.estado}")
                print(f"empresa: {proyecto.empresa}")
                print(f"gerente: {proyecto.gerente}")
                print(f"equipo: {proyecto.equipo}")
                print("tareas:")
                for i in proyecto.tareas:
                    print(f"- {i.nombre}")
                band =1
                break
            else: 
                band=0
                
        if band ==0:
            print("proyecto no encontrado")
        print("------------------------------")

    def eliminar_proyecto(self):
        m = input("ingrese el nombre del proyecto a eliminar: ")
        for i in self.proyectos:
            if m == i.nombre:
                self.proyectos.pop(i)
    
    def listar_proyectos(self):
        for i in self.proyectos:
            print(f"-{i.nombre}")