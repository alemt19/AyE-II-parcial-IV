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

    def modify_node_by_attribute(self, attribute, value, new_data):
        node_to_modify = self.find_node_by_attribute(attribute, value)
        if node_to_modify:
            node_to_modify.data.id = new_data.id
            node_to_modify.data.nombre = new_data.nombre
            node_to_modify.data.descripcion = new_data.descripcion
            node_to_modify.data.fecha_inicio = new_data.fecha_inicio
            node_to_modify.data.fecha_vencimiento = new_data.fecha_fin
            node_to_modify.data.estado = new_data.estado
            node_to_modify.data.empresa = new_data.empresa
            node_to_modify.data.porcentaje = new_data.porcentaje
            return True
        return False

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
            if self.root == node_to_delete:
                self.root = None
            else:
                parent_node = self.find_parent(self.root, node_to_delete)
                if parent_node:
                    parent_node.remove_child(node_to_delete)
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

def reportess(tree):
    print("\n1. Recorrer en postorden tareas de un proyecto")
    print("2. Listar sprints de un proyecto")
    option = int(input("Ingrese una opción: "))

    if option == 1:
        project_name = input("Ingrese el nombre del proyecto: ")
        project = tree.find_node_by_attribute('nombre', project_name)
        if project:
            tree.postorder_traversal(project)
            print()
        else:
            print("No se encontró el proyecto.")

    elif option == 2:
        project_name = input("Ingrese el nombre del proyecto: ")
        project = tree.find_node_by_attribute('nombre', project_name)
        if project:
            level = int(input("Ingrese la altura desde donde desea mostrar los sprints: "))
            nodes = tree.get_elements_at_level(level)
            for node in nodes:
                print(node)
        else:
            print("No se encontró el proyecto.")

    else:
        print("Opción no válida.")

def main_menu():
    tree = NaryTree("Proyecto Raíz")  # Crear árbol de ejemplo
    root_node = tree.root

    while True:
        print("\n--- Menú de Gestión de Proyecto ---")
        print("1. Agregar un nodo al árbol")
        print("2. Modificar un nodo")
        print("3. Eliminar un nodo")
        print("4. Mostrar el árbol")
        print("5. Buscar un nodo por atributo")
        print("6. Reportes")
        print("7. Salir")

        option = int(input("Seleccione una opción: "))

        if option == 1:
            parent_data = input("Ingrese el dato del nodo padre: ")
            parent_node = tree.find_node(parent_data)
            if parent_node:
                child_data = input("Ingrese el dato del nuevo nodo: ")
                tree.add_child_to_node(parent_node, child_data)
                print("Nodo agregado exitosamente.")
            else:
                print("Nodo padre no encontrado.")

        elif option == 2:
            attribute = input("Ingrese el atributo del nodo a modificar (por ejemplo, 'nombre'): ")
            value = input("Ingrese el valor del atributo del nodo a modificar: ")
            new_data = input("Ingrese los nuevos datos del nodo (formato: id,nombre,descripcion,fecha_inicio,fecha_vencimiento,estado,empresa,porcentaje): ").split(',')
            new_node_data = {
                'id': int(new_data[0]),
                'nombre': new_data[1],
                'descripcion': new_data[2],
                'fecha_inicio': new_data[3],
                'fecha_vencimiento': new_data[4],
                'estado': new_data[5],
                'empresa': new_data[6],
                'porcentaje': float(new_data[7])
            }
            success = tree.modify_node_by_attribute(attribute, value, new_node_data)
            if success:
                print("Nodo modificado exitosamente.")
            else:
                print("No se encontró el nodo o no se pudo modificar.")

        elif option == 3:
            attribute = input("Ingrese el atributo del nodo a eliminar (por ejemplo, 'nombre'): ")
            value = input("Ingrese el valor del atributo del nodo a eliminar: ")
            success = tree.delete_node_by_attribute(attribute, value)
            if success:
                print("Nodo eliminado exitosamente.")
            else:
                print("No se encontró el nodo o no se pudo eliminar.")

        elif option == 4:
            print("Árbol:")
            tree.display_tree(tree.root)

        elif option == 5:
            attribute = input("Ingrese el atributo del nodo a buscar (por ejemplo, 'nombre'): ")
            value = input("Ingrese el valor del atributo del nodo a buscar: ")
            node = tree.find_node_by_attribute(attribute, value)
            if node:
                print("Nodo encontrado:", node.data)
            else:
                print("No se encontró el nodo.")

        elif option == 6:
            reportess(tree)

        elif option == 7:
            print("Saliendo del menú.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
