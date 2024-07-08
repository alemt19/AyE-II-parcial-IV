import json
from datetime import datetime
from proyecto4.subtareas import Subtarea

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
        self.subtareas = [Subtarea for sub in self.subtareas if sub.id != id_subtarea]

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

    def mostrar_tareas_en_nivel(self, nivel):
        # Método para mostrar las tareas en un nivel específico
        if nivel == 0:
            print(f"Tareas del Proyecto {self.nombre}:")
            for tarea in self.tareas:
                print(f" - {tarea}")
        else:
            for tarea in self.tareas:
                print(f"Tarea {tarea.nombre}:")

    def _mostrar_subtareas_en_nivel(self, tarea, nivel_restante, indent):
        # Método auxiliar para mostrar las subtareas en un nivel específico
        for subtarea in tarea.subtareas:
            print(' ' * indent + f"- {subtarea}")
            if nivel_restante > 0:
                self._mostrar_subtareas_en_nivel(subtarea, nivel_restante - 1, indent + 2)

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
                "fecha_inicio": tarea.fecha_inicio,
                "fecha_vencimiento": tarea.fecha_vencimiento,
                "estado": tarea.estado,
                "empresa": tarea.empresa,
                "porcentaje": tarea.porcentaje,
                "subtareas": []
            }
            for subtarea in tarea.subtareas:
                subtarea_dict = {
                    "id": subtarea.id,
                    "nombre": subtarea.nombre,
                    "descripcion": subtarea.descripcion,
                    "estado": subtarea.estado
                }
                tarea_dict["subtareas"].append(subtarea_dict)
            proyecto_dict["tareas"].append(tarea_dict)
        return proyecto_dict

    @staticmethod
    def deserializar(proyecto_dict):
        # Método estático para deserializar un diccionario y crear un proyecto
        proyecto = Proyecto(proyecto_dict["nombre"])
        for tarea_dict in proyecto_dict["tareas"]:
            tarea = Tarea(
                tarea_dict["nombre"],
                tarea_dict["descripcion"],
                tarea_dict["fecha_inicio"],
                tarea_dict["fecha_vencimiento"],
                tarea_dict["estado"],
                tarea_dict["empresa"],
                tarea_dict["porcentaje"]
            )
            for subtarea_dict in tarea_dict["subtareas"]:
                subtarea = Tarea(
                    subtarea_dict["nombre"],
                    subtarea_dict["descripcion"],
                    subtarea_dict["estado"]
                )
                tarea.agregar_subtarea(subtarea)
            proyecto.agregar_tarea(tarea)
        return proyecto
