
class Subtarea:
    id = 0
    def __init__(self, nombre, descripcion, estado):
        Subtarea.id += 1
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado