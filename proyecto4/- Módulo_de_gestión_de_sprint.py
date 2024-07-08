from datetime import datetime

# Falta importar la clase Tarea

class Sprint:
    def __init__(self, nombre, fecha_inicio, fecha_fin, estado, objetivos, equipo):
        self.id = None  # El id se asignará al insertar en el árbol AVL
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.objetivos = objetivos
        self.equipo = equipo
        self.tareas = []  # Lista para almacenar las tareas del sprint

    def agregar_tarea(self, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, porcentaje):
        # Método para agregar una tarea al sprint
        tarea = {
            "id": len(self.tareas) + 1,
            "nombre": nombre,
            "descripcion": descripcion,
            "fecha_inicio": fecha_inicio,
            "fecha_vencimiento": fecha_vencimiento,
            "estado": estado,
            "empresa": empresa,
            "porcentaje": porcentaje
        }
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        # Método para mostrar las tareas asignadas al sprint
        if not self.tareas:
            print("No hay tareas asignadas a este sprint.")
        else:
            for tarea in self.tareas:
                print(f"- Tarea {tarea['id']}: {tarea['nombre']}")

    def eliminar_tarea(self, id_tarea):
        # Método para eliminar una tarea del sprint basada en su ID
        for tarea in self.tareas:
            if tarea["id"] == id_tarea:
                self.tareas.remove(tarea)
                return

    def __repr__(self):
        # Representación en forma de cadena del sprint
        return f"Sprint(id={self.id}, nombre='{self.nombre}', estado='{self.estado}')"

class NodoAVL:
    def __init__(self, sprint):
        self.sprint = sprint
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, sprint):
        # Método para insertar un sprint en el árbol AVL
        self.raiz = self._insertar(self.raiz, sprint)

    def _insertar(self, nodo, sprint):
        # Método recursivo para insertar un sprint en el árbol AVL
        if not nodo:
            return NodoAVL(sprint)
        if sprint.nombre < nodo.sprint.nombre:
            nodo.izquierda = self._insertar(nodo.izquierda, sprint)
        else:
            nodo.derecha = self._insertar(nodo.derecha, sprint)
        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        balance = self._balance(nodo)
        if balance > 1 and sprint.nombre < nodo.izquierda.sprint.nombre:
            return self._rotar_derecha(nodo)
        if balance < -1 and sprint.nombre > nodo.derecha.sprint.nombre:
            return self._rotar_izquierda(nodo)
        if balance > 1 and sprint.nombre > nodo.izquierda.sprint.nombre:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        if balance < -1 and sprint.nombre < nodo.derecha.sprint.nombre:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)
        return nodo

    def _altura(self, nodo):
        # Método para obtener la altura de un nodo
        if not nodo:
            return 0
        return nodo.altura

    def _balance(self, nodo):
        # Método para calcular el balance de un nodo
        if not nodo:
            return 0
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)

    def _rotar_izquierda(self, z):
        # Rotación a la izquierda
        y = z.derecha
        T3 = y.izquierda
        y.izquierda = z
        z.derecha = T3
        z.altura = 1 + max(self._altura(z.izquierda), self._altura(z.derecha))
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        return y

    def _rotar_derecha(self, z):
        # Rotación a la derecha
        y = z.izquierda
        T2 = y.derecha
        y.derecha = z
        z.izquierda = T2
        z.altura = 1 + max(self._altura(z.izquierda), self._altura(z.derecha))
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        return y

    def serializar(self):
        # Método para serializar el árbol AVL
        return self._serializar(self.raiz)

    def _serializar(self, nodo):
        # Método recursivo para serializar el árbol AVL
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
                "tareas": nodo.sprint.tareas
            }
        }
        nodo_serializado["izquierda"] = self._serializar(nodo.izquierda)
        nodo_serializado["derecha"] = self._serializar(nodo.derecha)
        return nodo_serializado

    @staticmethod
    def deserializar(sprints_json):
        # Método estático para deserializar el árbol AVL
        if not sprints_json:
            return ArbolAVL()
        arbol = ArbolAVL()
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
            sprint.tareas = sprint_dict["tareas"]
            arbol.insertar(sprint)
        return arbol
