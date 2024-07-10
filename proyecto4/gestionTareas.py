from datetime import datetime
from reportes_proyecto2 import NaryTree
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
        print("8. Salir")

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
                print("no se encontro el proyecto")
            else:
                print(tarea_encontrada.data)
        elif opcion == "3":
            tarea=str(input("ingrese el nombre de la tarea a eliminar: "))
            a=tree.delete_node_by_attribute('nombre',tarea)
            if a:
                print("eliminado exitosamente")
            else:
                print("no se pudo eliminar")

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
                tree.modify_node_by_attribute('nombre',starea,tarea)
                print("tarea actualizada correctamente")
                
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
class Proyecto:
    def __init__(self, nombre):
        # Constructor de la clase Proyecto
        self.nombre = nombre
        self.tareas = []  # Lista para almacenar tareas

    def agregar_tarea(self, tarea):
        # Método para agregar una tarea al proyecto
        self.tareas.append(tarea)

    def eliminar_tarea(self, id_tarea):
        # Método para eliminar una tarea basada en su ID
        self.tareas = [tarea for tarea in self.tareas if tarea.id != id_tarea]

    def agregar_subtarea_a_tarea(self, id_tarea, subtarea):
        # Método para agregar una subtarea a una tarea específica por ID de tarea
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                tarea.agregar_subtarea(subtarea)
                return

    def eliminar_subtarea_de_tarea(self, id_tarea, id_subtarea):
        # Método para eliminar una subtarea de una tarea específica por IDs
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                tarea.eliminar_subtarea(id_subtarea)
                return

    def listar_tareas(self):
        # Método para listar todas las tareas del proyecto
        print(f"Tareas del Proyecto {self.nombre}:")
        for tarea in self.tareas:
            self._mostrar_subtareas_en_nivel(tarea, 0, 2)

    def _mostrar_subtareas_en_nivel(self, tarea, nivel_restante, indent):
        # Método auxiliar para mostrar las subtareas en un nivel específico
        print(' ' * indent + f"- {tarea}")
        if nivel_restante > 0:
            for subtarea in tarea.subtareas:
                self._mostrar_subtareas_en_nivel(subtarea, nivel_restante - 1, indent + 2)

    def eliminar_subtarea(self, id_subtarea):
        # Método para eliminar una subtarea de cualquier tarea del proyecto
        for tarea in self.tareas:
            tarea.eliminar_subtarea(id_subtarea)

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

    def agregar_tarea_subtarea(self, nombre_tarea, subtarea):
        # Método para agregar una subtarea a una tarea específica por nombre de tarea
        for tarea in self.tareas:
            if tarea.nombre == nombre_tarea:
                tarea.agregar_subtarea(subtarea)
                return

    def consultar_tarea_por_nombre(self, nombre_tarea):
        # Método para consultar una tarea por su nombre
        for tarea in self.tareas:
            if tarea.nombre == nombre_tarea:
                return tarea
        return None

    def eliminar_tarea_por_nombre(self, nombre_tarea):
        # Método para eliminar una tarea por su nombre (y sus subtareas)
        self.tareas = [tarea for tarea in self.tareas if tarea.nombre != nombre_tarea]

    def eliminar_subtarea_de_todas_las_tareas(self, id_subtarea):
        # Método para eliminar una subtarea de todas las tareas del proyecto
        for tarea in self.tareas:
            tarea.eliminar_subtarea(id_subtarea)"""
