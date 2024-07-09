from datetime import datetime
from gestion_proyecto_arbolAVL import AVLTree

class Empresa:
    id = 1
    def __init__(self, nombre, descripcion, f_creacion, direccion, telefono, correo, gerente, equipo_contacto):
        self.id = Empresa.id
        Empresa.id += 1
        self.nombre = nombre
        self.descripcion = descripcion
        self.f_creacion = datetime.strptime(f_creacion, '%Y-%m-%d')
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.gerente = gerente
        self.equipo_contacto = equipo_contacto
        self.proyectos = AVLTree()
