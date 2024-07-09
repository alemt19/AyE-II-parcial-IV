from gestion_proyecto_arbolAVL import AVLTree
from listaEnlazada import LinkedList
class Tarea:
    def __init__(self, id_tarea, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, porcentaje):
        self.id = id_tarea
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.empresa = empresa
        self.porcentaje = porcentaje
        self.subtareas = LinkedList()  # Lista enlazada para subtareas

    def agregar_subtarea(self, subtarea):
        self.subtareas.append(subtarea)

    def mostrar_subtareas(self, nivel=0):
        print("  " * nivel + f"- {self.nombre}")
        current = self.subtareas.head
        while current:
            current.data.mostrar_subtareas(nivel + 1)
            current = current.next

class Sprint:
    def __init__(self, nombre, fecha_inicio, fecha_fin, estado, objetivos, equipo):
        self.id = None  # El id se asignará al insertar en el árbol AVL
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.objetivos = objetivos
        self.equipo = equipo
        self.tareas = LinkedList()  # Lista enlazada para almacenar las tareas del sprint

    def agregar_tarea(self, id_tarea, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, porcentaje):
        tarea = Tarea(id_tarea, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, porcentaje)
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        if not self.tareas.head:
            print("No hay tareas asignadas a este sprint.")
        else:
            current = self.tareas.head
            while current:
                print(f"- Tarea {current.data.id}: {current.data.nombre}")
                current = current.next

    def eliminar_tarea(self, id_tarea):
        current = self.tareas.head
        prev = None
        while current:
            if current.data.id == id_tarea:
                if prev:
                    prev.next = current.next
                else:
                    self.tareas.head = current.next
                break
            prev = current
            current = current.next

    def mostrar_tareas_disponibles(self, tareas_proyecto):
        disponibles = []
        for tarea in tareas_proyecto:
            if not any(tarea.data.id == tarea_sprint.data.id for tarea_sprint in self.tareas):
                if tarea.data.estado != "completada":
                    disponibles.append(tarea.data)
        if not disponibles:
            print("No hay tareas disponibles para agregar.")
        else:
            for tarea in disponibles:
                print(f"- Tarea {tarea.id}: {tarea.nombre}")

    def mostrar_subtareas_de_tarea(self, id_tarea):
        current = self.tareas.head
        while current:
            if current.data.id == id_tarea:
                print(f"Subtareas de {current.data.nombre}:")
                current.data.mostrar_subtareas(1)
                return
            current = current.next
        print(f"No se encontró la tarea con ID {id_tarea} en este sprint.")

    def __repr__(self):
        return f"Sprint(id={self.id}, nombre='{self.nombre}', estado='{self.estado}')"

    def serializar(self):
        return self._serializar(self.raiz)

    def _serializar(self, nodo):
        if not nodo:
            return None
        nodo_serializado = {
            "sprint": {
                "id": nodo.sprint.id,
                "nombre": nodo.sprint.nombre,
                "fecha_inicio": nodo.sprint.fecha_inicio,
                "fecha_fin": nodo.sprint.fecha_fin,
                "estado": nodo.sprint.estado,
                "objetivos": nodo.sprint.objetivos,
                "equipo": nodo.sprint.equipo,
                "tareas": [tarea.id for tarea in nodo.sprint.tareas]
            }
        }
        nodo_serializado["izquierda"] = self._serializar(nodo.izquierda)
        nodo_serializado["derecha"] = self._serializar(nodo.derecha)
        return nodo_serializado

    @staticmethod
    def deserializar(sprints_json):
        if not sprints_json:
            return AVLTree()
        arbol = AVLTree()
        for sprint_dict in sprints_json:
            sprint = Sprint(
                sprint_dict["nombre"],
                sprint_dict["fecha_inicio"],
                sprint_dict["fecha_fin"],
                sprint_dict["estado"],
                sprint_dict["objetivos"],
                sprint_dict["equipo"]
            )
            sprint.id = sprint_dict["id"]
            arbol.insertar(sprint)
            for tarea_id in sprint_dict["tareas"]:
                tarea = obtener_tarea_por_id(tarea_id)  # Función para obtener la tarea por ID
                if tarea:
                    sprint.agregar_tarea(tarea.id, tarea.nombre, tarea.descripcion, tarea.fecha_inicio,
                                         tarea.fecha_vencimiento, tarea.estado, tarea.empresa, tarea.porcentaje)
        return arbol

