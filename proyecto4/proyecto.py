from datetime import datetime
from gestion_proyecto_arbolAVL import AVLTree

class Proyecto:
    id = 1  # Variable de clase para mantener el contador de IDs

    def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin, estado_actual, empresa, gerente, equipo):
        self.id = Proyecto.id  # Asignar el ID actual al proyecto
        Proyecto.id += 1  # Incrementar el contador de IDs para el próximo proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        self.fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
        self.estado_actual = estado_actual
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
        self.sprint= AVLTree()
    
    def __str__(self):
        return f"Proyecto(id={self.id}, nombre={self.nombre}, fecha_vencimiento={self.fecha_fin}, estado_actual={self.estado_actual})"
    
    @property
    def tiempo_restante(self):
        return (self.fecha_fin - datetime.now()).days
    
    def __lt__(self, other):
        return self.id < other.id

    def __le__(self, other):
        return self.id <= other.id

    def __gt__(self, other):
        return self.id > other.id

    def __ge__(self, other):
        return self.id >= other.id

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id
