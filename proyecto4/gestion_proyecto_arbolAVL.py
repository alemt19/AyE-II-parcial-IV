from datetime import datetime
class AVLNode:
    def __init__(self, key, left=None, right=None, height=1):
        self.key = key
        self.left = left
        self.right = right
        self.height = height

    def __str__(self, level=0, prefix="Root: "):
        result = " " * (level * 4) + prefix + str(self.key) + "\n"
        if self.left:
            result += self.left.__str__(level + 1, "L--- ")
        if self.right:
            result += self.right.__str__(level + 1, "R--- ")
        return result

class AVLTree:

    def __init__(self):
        self.root = None

    def postorder_traversal(self):
        nodes = []
        self._postorder_traversal(self.root, nodes)
        return nodes

    def _postorder_traversal(self, node, nodes):
        if node:
            self._postorder_traversal(node.left, nodes)
            self._postorder_traversal(node.right, nodes)
            nodes.append(node.key)

    def preorder_traversal(self):
        nodes = []
        self._preorder_traversal(self.root, nodes)
        return nodes

    def _preorder_traversal(self, node, nodes):
        if node:
            nodes.append(node.key)
            self._preorder_traversal(node.left, nodes)
            self._preorder_traversal(node.right, nodes)
    
    def __str__(self):
        if not self.root:
            return "Empty tree"
        return str(self.root)

    def insert(self, key):
        if not self.root:
            self.root = AVLNode(key)
        else:
            self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)
    
    

    def _balance(self, node):
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def get_nodes_at_height(self, height):
        nodes = []
        self._get_nodes_at_height(self.root, height, 0, nodes)
        return nodes

    def _get_nodes_at_height(self, node, target_height, current_height, nodes):
        if not node:
            return
        if current_height == target_height:
            nodes.append(node.key)
        else:
            self._get_nodes_at_height(node.left, target_height, current_height + 1, nodes)
            self._get_nodes_at_height(node.right, target_height, current_height + 1, nodes)
    
    
    
    def eliminar(self, nombre_proyecto):
        if self.root:
            self.root = self._eliminar(self.root, nombre_proyecto)
    
    def _eliminar(self, node, nombre_proyecto):
        if not node:
            return node
        if nombre_proyecto < node.key.nombre:
            node.left = self._eliminar(node.left, nombre_proyecto)
        elif nombre_proyecto > node.key.nombre:
            node.right = self._eliminar(node.right, nombre_proyecto)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.right = self._eliminar(node.right, temp.key.nombre)
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)
    
    def buscar_proyecto(self, criteria, value):
        if not self.root:
            return None
        if criteria == 'id' and self.root.key.id == value:
            return self.root
        elif criteria == 'nombre' and self.root.key.nombre == value:
            return self.root
        elif criteria == 'gerente' and self.root.key.gerente == value:
            return self.root
        elif criteria == 'fecha_inicio' and self.root.key.fecha_inicio == value:
            return self.root
        elif criteria == 'fecha_vencimiento' and self.root.key.fecha_vencimiento == value:
            return self.root
        elif criteria == 'estado_actual' and self.root.key.estado_actual == value:
            return self.root
        
        left_search = self.buscar_proyecto(self.root.left, criteria, value)
        if left_search:
            return left_search
        return self.buscar_proyecto(self.root.right, criteria, value)
    
    
    def inorder_traversal(self):
        nodes = []
        self._inorder_traversal(self.root, nodes)
        return nodes

    def _inorder_traversal(self, node, nodes):
        if node:
            self._inorder_traversal(node.left, nodes)
            nodes.append(node.key)
            self._inorder_traversal(node.right, nodes)
    


def consulta_proyecto(tree):
    while True:
        print("\n--- Menú de Consulta de Proyectos ---")
        print("1. Consultar por ID")
        print("2. Consultar por Nombre")
        print("3. Consultar por Gerente")
        print("4. Consultar por Fecha de Inicio")
        print("5. Consultar por Fecha de Vencimiento")
        print("6. Consultar por Estado Actual")
        print("7. Volver al Menú Principal")
        opcion = input("Seleccione un criterio: ")

        if opcion == "1":
            id_proyecto = int(input("ID del proyecto a consultar: "))
            result = tree.buscar_proyecto( 'id', id_proyecto)
        elif opcion == "2":
            nombre = input("Nombre del proyecto a consultar: ")
            result = tree.buscar_proyecto( 'nombre', nombre)
        elif opcion == "3":
            gerente = input("Gerente del proyecto a consultar: ")
            result = tree.buscar_proyecto( 'gerente', gerente)
        elif opcion == "4":
            fecha_inicio = datetime.strptime(input("Fecha de inicio del proyecto a consultar (YYYY-MM-DD): "), '%Y-%m-%d')
            result = tree.buscar_proyecto( 'fecha_inicio', fecha_inicio)
        elif opcion == "5":
            fecha_vencimiento = datetime.strptime(input("Fecha de vencimiento del proyecto a consultar (YYYY-MM-DD): "), '%Y-%m-%d')
            result = tree.buscar_proyecto( 'fecha_vencimiento', fecha_vencimiento)
        elif opcion == "6":
            estado_actual = input("Estado actual del proyecto a consultar: ")
            result = tree.buscar_proyecto('estado_actual', estado_actual)
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            continue

        if result:
            print(result.key)
        else:
            print("Proyecto no encontrado")

def menu(tree):
    
    while True:
        print("\n--- Menú de Proyectos ---")
        print("1. Agregar proyecto")
        print("2. Consultar proyecto")
        print("3. Listar todos los proyectos")
        print("4. Eliminar proyecto por nombre")
        print("5. Actualizar tiempos restantes")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            from proyecto import Proyecto
            nombre = input("Nombre del proyecto: ")
            descripcion = input("Descripción del proyecto: ")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
            estado_actual = input("Estado actual: ")
            empresa = input("Empresa: ")
            gerente = input("Gerente: ")
            equipo = input("Equipo (separado por comas): ").split(", ")
            proyecto = Proyecto(nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, empresa, gerente, equipo)
            tree.insert(proyecto)
            print("Proyecto agregado exitosamente.")

        elif opcion == "2":
            consulta_proyecto(tree)

        elif opcion == "3":
            print("Lista de proyectos:")
            inorder_elements = avl.inorder_traversal()
            print(f"Elementos en el árbol en orden: {[str(node) for node in inorder_elements]} \n")

        elif opcion == "4":
            nombre = input("Nombre del proyecto a eliminar: ")
            tree.eliminar(nombre)
            print("Proyecto eliminado exitosamente.")

        elif opcion == "5":
            print("Actualizando tiempos restantes...")
            print("Tiempos restantes actualizados.")

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

avl = AVLTree()
menu(avl)



