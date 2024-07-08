import json
from datetime import datetime

class Tarea:
    id_counter = 0

    def __init__(self, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, porcentaje):
        # Constructor de la clase Tarea
        Tarea.id_counter += 1
        self.id = Tarea.id_counter
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.empresa = empresa
        self.porcentaje = porcentaje
        self.subtareas = []  # Lista para almacenar subtareas

    def agregar_subtarea(self, subtarea):
        # Método para agregar una subtarea a la tarea
        self.subtareas.append(subtarea)

    def eliminar_subtarea(self, id_subtarea):
        # Método para eliminar una subtarea basada en su ID
        self.subtareas = [subtarea for subarea in self.subtareas if subarea.id != id_subtarea]

    def __repr__(self):
        # Representación en forma de cadena de la tarea
        return f"Tarea(id={self.id}, nombre='{self.nombre}', estado='{self.estado}')"

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
                "fecha_vencimiento": tarea.fecha_vencimiento.strftime('%Y-%m-%d') if tarea.fecha_vencimiento else None,
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
                datetime.strptime(tarea_dict["fecha_vencimiento"], '%Y-%m-%d') if tarea_dict["fecha_vencimiento"] else None,
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
            tarea.eliminar_subtarea(id_subtarea)
