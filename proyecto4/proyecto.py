from datetime import datetime
import pila as pi
import cola as co
class Proyecto: 
    id=0
    def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin, estado, empresa, gerente, equipo):
        Proyecto.id += 1
        self.id = Proyecto.id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
        self.tareas=[]
        self.tareas_prioritarias = pi.Pila()
        self.tareas_proximas_avencer=co.Cola()
