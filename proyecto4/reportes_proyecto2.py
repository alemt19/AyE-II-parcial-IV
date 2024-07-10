from datetime import datetime

class NaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]

    def add_child(self, child_node):
        self.children.append(child_node)

class NaryTree:
    def __init__(self, root_data):
        self.root = NaryTreeNode(root_data)

    def add_child_to_node(self, parent_node, child_data):
        child_node = NaryTreeNode(child_data)
        parent_node.add_child(child_node)
        return child_node

    def preorder_traversal(self, node):
        if node:
            print(node.data, end=" ")
            for child in node.children:
                self.preorder_traversal(child)

    def postorder_traversal(self, node):
        if node:
            for child in node.children:
                self.postorder_traversal(child)
            print(node.data, end=" ")

    def find_depth(self, node):
        if not node:
            return 0
        if not node.children:
            return 1
        else:
            return 1 + max(self.find_depth(child) for child in node.children)
    def find_parent(self, current_node, target_node):
        if not current_node:
            return None
        for child in current_node.children:
            if child == target_node:
                return current_node
            parent = self.find_parent(child, target_node)
            if parent:
                return parent
        return None

    def delete_node(self, target_node):
        if self.root == target_node:
            self.root = None
        else:
            parent_node = self.find_parent(self.root, target_node)
            if parent_node:
                parent_node.remove_child(target_node)

    def get_elements_at_level(self, level):
        if not self.root:
            return []
        if level == 0:
            return [self.root.data]
        
        current_level = 0
        queue = [self.root]
        
        while queue:
            next_queue = []
            current_level += 1
            for node in queue:
                next_queue.extend(node.children)
            if current_level == level:
                return [child.data for child in next_queue]
            queue = next_queue
        
        return []
    def display_tree(self, node, level=0):
        if node:
            print(' ' * level * 2 + str(node.data))
            for child in node.children:
                self.display_tree(child, level + 1)
    
    def find_node(self, data):
        return self._find_node_recursive(self.root, data)
    
    def _find_node_recursive(self, node, data):
        if node is None:
            return None
        if node.data == data:
            return node
        for child in node.children:
            result = self._find_node_recursive(child, data)
            if result:
                return result
        return None
    
    def find_node_by_attribute(self, attribute, value):
        return self._find_node_by_attribute_recursive(self.root, attribute, value)
    
    def _find_node_by_attribute_recursive(self, node, attribute, value):
        if node is None:
            return None
        if getattr(node.data, attribute, None) == value:
            return node
        for child in node.children:
            result = self._find_node_by_attribute_recursive(child, attribute, value)
            if result:
                return result
        return None
    
    def delete_node_by_attribute(self, attribute, value):
        node_to_delete = self.find_node_by_attribute(attribute, value)
        if node_to_delete:
            self.delete_node(node_to_delete)
            return True
        return False
    
    def inorder_traversal(self, node):
        result = []
        self._inorder_traversal_recursive(node, result)
        return result

    def _inorder_traversal_recursive(self, node, result):
        if node:
            for child in node.children:
                self._inorder_traversal_recursive(child, result)
            result.append(node.data)
    
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

            
    