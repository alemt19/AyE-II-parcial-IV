class Tareas: 
    id=0
    def __init__(self, nombre, empresa, cliente, descripcion, fecha_de_inicio, fecha_de_vencimiento, estado, porcentaje):

        Tareas.id += 1
        self.id = Tareas.id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_de_inicio
        self.fecha_fin = fecha_de_vencimiento
        self.estado = estado
        self.empresa = empresa
        self.cliente = cliente
        self.porcentaje=porcentaje
        self.subtareas=[]