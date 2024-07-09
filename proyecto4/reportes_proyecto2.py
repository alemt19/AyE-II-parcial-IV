from datetime import datetime

class NaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

class NaryTree:
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root = NaryTreeNode(root_value)
        else:
            self.root = None

    def set_root(self, root_value):
        self.root = NaryTreeNode(root_value)

    def __repr__(self):
        return repr(self.root) if self.root is not None else 'Empty Tree'

    
def reportess(arbolProyecto):
    print("1. recorrer en postorden tareas de un proyecto")
    print("2. listar sprites de un proyecto")
    x = int(input("Ingrese una opcion: "))

    if x == 1:   
        p= str(input("ingrese el nombre del proyecto: "))  
        proyecto=arbolProyecto.buscar_proyecto('nombre',p)
        nodos=proyecto.sprint.mostrar_tareas()

    elif x == 2:
        p= str(input("ingrese el nombre del proyecto: "))  
        proyecto=arbolProyecto.buscar_proyecto('nombre',p)
        if proyecto is None:
            print("no se encontro el proyecto")
        else:
            a=int(input("ingrese la altura desde donde desea mostrar los sprites: "))
            nodos=proyecto.sprint.get_nodes_at_height(a)
            for i in nodos:
                i.mostrar_tareas()
                
    else:
        print("No se han encontrado tareas que cumplan con las condiciones dadas.")

            
    