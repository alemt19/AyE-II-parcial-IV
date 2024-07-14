class Subtarea:
    id = 1
    def __init__(self, nombre, descripcion, estado):
        self.id = Subtarea.id  # Asignar el ID actual al proyecto
        Subtarea.id += 1
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
    
    def __repr__(self):
        # Representación en forma de cadena de la subtarea
        return f"Subtarea(id={self.id}, nombre='{self.nombre}', descripción='{self.descripcion}', estado='{self.estado}')"