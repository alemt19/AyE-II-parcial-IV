from datetime import datetime
from reportes_proyecto2 import NaryTree
from subtarea import Subtarea
class Tarea:
    id_counter = 0

    def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin, estado, empresa, porcentaje):
        # Constructor de la clase Tarea
        Tarea.id_counter += 1
        self.id = Tarea.id_counter
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        self.fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
        self.estado = estado
        self.empresa = empresa
        self.porcentaje = porcentaje
        self.subtareas = NaryTree(None) # Lista para almacenar subtareas
    
    def __repr__(self):
        # Representación en forma de cadena de la tarea
        return f"Tarea(id={self.id}, nombre='{self.nombre}', estado='{self.estado}')"
    
def menu(tree):
    while True:
        print("\n--- Menú de Gestión de Tareas ---")
        print("1. Agregar tarea")
        print("2. Consultar tarea")
        print("3. eliminar tarea")
        print("4. Listar tareas")
        print("5. modificar tarea")
        print("6. Mostrar tareas por nivel")
        print("7. Mostrar árbol de tareas")
        print("8. Gestionar subtareas")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            name = input("Nombre de la tarea: ")
            description = input("Descripción: ")
            start_date = str(input("Fecha de inicio: "))
            due_date = str(input("Fecha de vencimiento: "))
            status = input("Estado actual: ")
            empresa=input("Empresa: ")
            progress = input("Porcentaje completado: ")
            tarea=Tarea(name,description,start_date,due_date,status,empresa,progress)
            tree.add_child_to_node(tree.root, tarea)
            
        elif opcion == "2":
            tarea=str(input("ingrese el nombre de la tarea a consultar: "))
            tarea_encontrada=tree.find_node_by_attribute('nombre',tarea)
            if tarea_encontrada is None:
                print("no se encontro la tarea")
            else:
                print(tarea_encontrada.data)
        elif opcion == "3":
            tarea=input("ingrese el nombre de la tarea a eliminar: ")
            t=tree.find_node_by_attribute('nombre', tarea)
            a = tree.delete_node(t)
            print("eliminado exitosamente")

        elif opcion == "4":
            resultado= tree.inorder_traversal(tree.root)
            for i in resultado:
                print("-",i,'\n')
        elif opcion == "5":
            starea=str(input("ingrese el nombre de la tarea a modificar: "))
            tarea_encontrada=tree.find_node_by_attribute('nombre',starea)
            if tarea_encontrada is None:
                print("no se encontro el proyecto")
            else:
                name = input("Nombre de la tarea: ")
                description = input("Descripción: ")
                start_date = str(input("Fecha de inicio: "))
                due_date = str(input("Fecha de vencimiento: "))
                status = input("Estado actual: ")
                empresa=input("Empresa: ")
                progress = input("Porcentaje completado: ")
                tarea=Tarea(name,description,start_date,due_date,status,empresa,progress)
                tarea.id = tree.find_node_by_attribute("nombre", starea).data.id
                tree.modify_node_by_attribute('nombre',starea,tarea)
                print("tarea actualizada correctamente")
                
        elif opcion == "6":
            nivel= int(input("ingrese el nivel: "))
            for i in tree.get_elements_at_level(nivel):
                print(i)
        elif opcion == "7":
            tree.display_tree(tree.root)
        elif opcion == "8":
            tarea=str(input("ingrese el nombre de la tarea de la cual desea gestionar sus subtareas: "))
            tarea_encontrada=tree.find_node_by_attribute('nombre',tarea)
            if tarea_encontrada:
                menuSubtareas(tarea_encontrada.data.subtareas)
            else:
                print("No se ha encontrado la tarea")
        elif opcion == "9":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def menuSubtareas(tree):
     while True:
        print("\n--- Menú de Gestión de Tareas ---")
        print("1. Agregar subtarea")
        print("2. Consultar subtarea")
        print("3. eliminar subtarea")
        print("4. Listar subtareas")
        print("5. modificar subtarea")
        print("6. Mostrar subtareas por nivel")
        print("7. Mostrar árbol de subtareas")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
                name = input("Nombre de la subtarea: ")
                description = input("Descripción: ")
                status = input("Estado actual: ")
                subtarea=Subtarea(name,description,status)
                tree.add_child_to_node(tree.root, subtarea)
        elif opcion == "2":
            subtarea=str(input("ingrese el nombre de la subtarea a consultar: "))
            subtarea_encontrada=tree.find_node_by_attribute('nombre',subtarea)
            print(subtarea_encontrada.__class__.__name__)
            if subtarea_encontrada:
                print("no se encontro la subtarea")
            else:
                print(subtarea_encontrada.data)
        elif opcion == "3":
            subtarea=input("ingrese el nombre de la subtarea a eliminar: ")
            t=tree.find_node_by_attribute('nombre', subtarea)
            a = tree.delete_node(t)
            print("eliminado exitosamente")

        elif opcion == "4":
            resultado= tree.inorder_traversal(tree.root)
            for i in resultado:
                print("-",i,'\n')
        elif opcion == "5":
            starea=str(input("ingrese el nombre de la subtarea a modificar: "))
            tarea_encontrada=tree.find_node_by_attribute('nombre',starea)
            if tarea_encontrada is None:
                print("no se encontro la subtarea")
            else:
                name = input("Nombre de la subtarea: ")
                description = input("Descripción: ")
                status = input("Estado actual: ")
                tarea=Tarea(name,description,status)
                tarea.id = tree.find_node_by_attribute("nombre", starea).data.id
                tree.modify_node_by_attribute('nombre',starea,tarea)
                print("subtarea actualizada correctamente")
                
        elif opcion == "6":
            nivel= int(input("ingrese el nivel: "))
            for i in tree.get_elements_at_level(nivel):
                print(i)
        elif opcion == "7":
            tree.display_tree(tree.root)
        elif opcion == "8":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
            
"""
    def serializar(self):
        # Método para serializar el proyecto a un diccionario
        proyecto_dict = {
            "nombre": self.nombre,
            "tareas": []
        }
        for tarea in self.tareas:
            tarea_dict = {
                "id": tarea.id,
                "nombre": tarea.nombre,
                "descripcion": tarea.descripcion,
                "fecha_inicio": tarea.fecha_inicio.strftime('%Y-%m-%d') if tarea.fecha_inicio else None,
                "fecha_fin": tarea.fecha_fin.strftime('%Y-%m-%d') if tarea.fecha_fin else None,
                "estado": tarea.estado,
                "empresa": tarea.empresa,
                "porcentaje": tarea.porcentaje,
                "subtareas": self._serializar_subtareas(tarea.subtareas)
            }
            proyecto_dict["tareas"].append(tarea_dict)
        return proyecto_dict

    def _serializar_subtareas(self, subtareas):
        # Método auxiliar para serializar las subtareas a un diccionario
        subtareas_dict = []
        for subtarea in subtareas:
            subtarea_dict = {
                "id": subtarea.id,
                "nombre": subtarea.nombre,
                "descripcion": subtarea.descripcion,
                "estado": subtarea.estado
            }
            if subtarea.subtareas:
                subtarea_dict["subtareas"] = self._serializar_subtareas(subtarea.subtareas)
            subtareas_dict.append(subtarea_dict)
        return subtareas_dict

    @staticmethod
    def deserializar(proyecto_dict):
        # Método estático para deserializar un diccionario y crear un proyecto
        proyecto = Proyecto(proyecto_dict["nombre"])
        for tarea_dict in proyecto_dict["tareas"]:
            tarea = Tarea(
                tarea_dict["nombre"],
                tarea_dict["descripcion"],
                datetime.strptime(tarea_dict["fecha_inicio"], '%Y-%m-%d') if tarea_dict["fecha_inicio"] else None,
                datetime.strptime(tarea_dict["fecha_fin"], '%Y-%m-%d') if tarea_dict["fecha_fin"] else None,
                tarea_dict["estado"],
                tarea_dict["empresa"],
                tarea_dict["porcentaje"]
            )
            if "subtareas" in tarea_dict:
                proyecto._deserializar_subtareas(tarea_dict["subtareas"], tarea)
            proyecto.agregar_tarea(tarea)
        return proyecto

    def _deserializar_subtareas(self, subtareas_dict, tarea_padre):
        # Método auxiliar para deserializar subtareas y agregarlas a una tarea padre
        for subtarea_dict in subtareas_dict:
            subtarea = Tarea(
                subtarea_dict["nombre"],
                subtarea_dict["descripcion"],
                None,  # Las subtareas no necesitan fecha de inicio ni vencimiento
                None,
                subtarea_dict["estado"],
                "",
                0  # Las subtareas no tienen porcentaje completado inicialmente
            )
            if "subtareas" in subtarea_dict:
                self._deserializar_subtareas(subtarea_dict["subtareas"], subtarea)
            tarea_padre.agregar_subtarea(subtarea)
"""
