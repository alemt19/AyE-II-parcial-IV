from listaEnlazada import LinkedList
from gestion_proyecto_arbolAVL import AVLTree

class Menu:
    def __init__(self):
        self.sprints = LinkedList()  # Lista enlazada para guardar instancias de Sprint
        self.tareas_proyecto = LinkedList()  # Lista enlazada para guardar instancias de Tarea del proyecto

    def agregar_sprint(self, sprint):
        self.sprints.append(sprint)

    def encontrar_sprint(self, nombre):
        current = self.sprints.head
        while current:
            if current.data.nombre == nombre:
                return current.data
            current = current.next
        return None

    def encontrar_tarea(self, id_tarea):
        current = self.tareas_proyecto.head
        while current:
            if current.data.id == id_tarea:
                return current.data
            current = current.next
        return None

    def menu(self):
        while True:
            print("\n--- Menú de Gestión de Sprint y Tareas ---")
            print("1. Agregar un sprint")
            print("2. Agregar una tarea al proyecto")
            print("3. Agregar una tarea a un sprint")
            print("4. Mostrar las tareas de un sprint")
            print("5. Eliminar una tarea de un sprint")
            print("6. Mostrar las subtareas de una tarea en un sprint")
            print("7. Mostrar tareas disponibles para agregar a un sprint")
            print("8. Mostrar todos los sprints")
            print("9. Salir")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                nombre = input("Ingrese el nombre del sprint: ")
                fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
                estado = input("Ingrese el estado del sprint: ")
                objetivos = input("Ingrese los objetivos del sprint: ")
                equipo = input("Ingrese el equipo del sprint: ")
                sprint = sprint(nombre, fecha_inicio, fecha_fin, estado, objetivos, equipo)
                self.agregar_sprint(sprint)
                print("Sprint agregado exitosamente.")

            elif opcion == 2:
                id_tarea = int(input("Ingrese el ID de la tarea: "))
                nombre = input("Ingrese el nombre de la tarea: ")
                descripcion = input("Ingrese la descripción de la tarea: ")
                fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
                estado = input("Ingrese el estado de la tarea: ")
                empresa = input("Ingrese la empresa: ")
                porcentaje = float(input("Ingrese el porcentaje completado: "))
                tarea = tarea(id_tarea, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, porcentaje)
                self.tareas_proyecto.append(tarea)
                print("Tarea agregada al proyecto exitosamente.")

            elif opcion == 3:
                nombre_sprint = input("Ingrese el nombre del sprint: ")
                sprint = self.encontrar_sprint(nombre_sprint)
                if sprint:
                    id_tarea = int(input("Ingrese el ID de la tarea: "))
                    nombre = input("Ingrese el nombre de la tarea: ")
                    descripcion = input("Ingrese la descripción de la tarea: ")
                    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                    fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
                    estado = input("Ingrese el estado de la tarea: ")
                    empresa = input("Ingrese la empresa: ")
                    porcentaje = float(input("Ingrese el porcentaje completado: "))
                    tarea = tarea(id_tarea, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, porcentaje)
                    sprint.agregar_tarea(id_tarea, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, porcentaje)
                    print("Tarea agregada al sprint exitosamente.")
                else:
                    print("Sprint no encontrado.")

            elif opcion == 4:
                nombre_sprint = input("Ingrese el nombre del sprint: ")
                sprint = self.encontrar_sprint(nombre_sprint)
                if sprint:
                    sprint.mostrar_tareas()
                else:
                    print("Sprint no encontrado.")

            elif opcion == 5:
                nombre_sprint = input("Ingrese el nombre del sprint: ")
                sprint = self.encontrar_sprint(nombre_sprint)
                if sprint:
                    id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
                    sprint.eliminar_tarea(id_tarea)
                else:
                    print("Sprint no encontrado.")

            elif opcion == 6:
                nombre_sprint = input("Ingrese el nombre del sprint: ")
                sprint = self.encontrar_sprint(nombre_sprint)
                if sprint:
                    id_tarea = int(input("Ingrese el ID de la tarea: "))
                    sprint.mostrar_subtareas_de_tarea(id_tarea)
                else:
                    print("Sprint no encontrado.")

            elif opcion == 7:
                nombre_sprint = input("Ingrese el nombre del sprint: ")
                sprint = self.encontrar_sprint(nombre_sprint)
                if sprint:
                    sprint.mostrar_tareas_disponibles(self.tareas_proyecto)
                else:
                    print("Sprint no encontrado.")

            elif opcion == 8:
                print("Sprints disponibles:")
                current = self.sprints.head
                if not current:
                    print("No hay sprints disponibles.")
                while current:
                    print(current.data)
                    current = current.next

            elif opcion == 9:
                print("Saliendo del menú.")
                break

            else:
                print("Opción no válida. Intente de nuevo.")
