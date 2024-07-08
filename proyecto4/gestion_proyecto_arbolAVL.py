from datetime import datetime

class AVLNode:
    def __init__(self, proyecto):
        self.proyecto = proyecto
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, proyecto):
        if not root:
            return AVLNode(proyecto)
        if proyecto.tiempo_restante < root.proyecto.tiempo_restante:
            root.left = self.insert(root.left, proyecto)
        else:
            root.right = self.insert(root.right, proyecto)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and proyecto.tiempo_restante < root.left.proyecto.tiempo_restante:
            return self.right_rotate(root)
        if balance < -1 and proyecto.tiempo_restante >= root.right.proyecto.tiempo_restante:
            return self.left_rotate(root)
        if balance > 1 and proyecto.tiempo_restante >= root.left.proyecto.tiempo_restante:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and proyecto.tiempo_restante < root.right.proyecto.tiempo_restante:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, nombre):
        if not root:
            return root
        if nombre < root.proyecto.nombre:
            root.left = self.delete(root.left, nombre)
        elif nombre > root.proyecto.nombre:
            root.right = self.delete(root.right, nombre)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.proyecto = temp.proyecto
            root.right = self.delete(root.right, temp.proyecto.nombre)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, nombre):
        if not root or root.proyecto.nombre == nombre:
            return root
        if nombre < root.proyecto.nombre:
            return self.search(root.left, nombre)
        return self.search(root.right, nombre)

    def update_remaining_times(self, root):
        if root:
            root.proyecto.tiempo_restante  # Al acceder a esta propiedad, se recalcula automáticamente
            self.update_remaining_times(root.left)
            self.update_remaining_times(root.right)

    def list_projects(self, root):
        if root:
            self.list_projects(root.left)
            print(root.proyecto)
            self.list_projects(root.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)
    def buscar_proyecto(self, root, criteria, value):
        if not root:
            return None
        if criteria == 'id' and root.proyecto.id == value:
            return root
        elif criteria == 'nombre' and root.proyecto.nombre == value:
            return root
        elif criteria == 'gerente' and root.proyecto.gerente == value:
            return root
        elif criteria == 'fecha_inicio' and root.proyecto.fecha_inicio == value:
            return root
        elif criteria == 'fecha_vencimiento' and root.proyecto.fecha_vencimiento == value:
            return root
        elif criteria == 'estado_actual' and root.proyecto.estado_actual == value:
            return root
        
        left_search = self.search_by_criteria(root.left, criteria, value)
        if left_search:
            return left_search
        return self.search_by_criteria(root.right, criteria, value)

def consulta_proyecto(tree, root):
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
            result = tree.buscar_proyecto(root, 'id', id_proyecto)
        elif opcion == "2":
            nombre = input("Nombre del proyecto a consultar: ")
            result = tree.buscar_proyecto(root, 'nombre', nombre)
        elif opcion == "3":
            gerente = input("Gerente del proyecto a consultar: ")
            result = tree.buscar_proyecto(root, 'gerente', gerente)
        elif opcion == "4":
            fecha_inicio = datetime.strptime(input("Fecha de inicio del proyecto a consultar (YYYY-MM-DD): "), '%Y-%m-%d')
            result = tree.buscar_proyecto(root, 'fecha_inicio', fecha_inicio)
        elif opcion == "5":
            fecha_vencimiento = datetime.strptime(input("Fecha de vencimiento del proyecto a consultar (YYYY-MM-DD): "), '%Y-%m-%d')
            result = tree.buscar_proyecto(root, 'fecha_vencimiento', fecha_vencimiento)
        elif opcion == "6":
            estado_actual = input("Estado actual del proyecto a consultar: ")
            result = tree.buscar_proyecto(root, 'estado_actual', estado_actual)
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            continue

        if result:
            print(result.proyecto)
        else:
            print("Proyecto no encontrado")