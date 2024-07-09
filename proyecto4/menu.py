import gestion_proyecto_arbolAVL as gestionProyecto
from proyecto import Proyecto
from gestionEmpresas import ListaEnlazada
import gestionEmpresas

def menu():
    tree = gestionProyecto.AVLTree()
    root = None
    empresas = ListaEnlazada()

    while True:
        # Menú principal
        print("\n--- Menú de Principal ---")
        print("1. Gestión de empresas")
        print("2. Gestión de proyectos")
        print("3. Gestión de tareas y prioridades")
        print("4. Gestión de sprints")
        print("5. Reportes")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                # Menú de empresas
                print("\n--- Menú de Empresas ---")
                print("1. Agregar empresa")
                print("2. Consultar empresa")
                print("3. Listar todas las empresas")
                print("4. Eliminar empresa por nombre")
                print("5. Modificar empresa")
                print("6. Salir")
                opcion = input("Seleccione una opción: ")
                
                if opcion == "1":
                    gestionEmpresas.crear_empresa(empresas)
                elif opcion == "2":
                    gestionEmpresas.consultar_empresa(empresa)
                elif opcion == "3":
                    gestionEmpresas.listar_empresas(empresas)
                elif opcion == "4":
                    gestionEmpresas.eliminar_empresa(empresas)
                elif opcion == "5":
                    gestionEmpresas.eliminar_empresas
                elif opcion == "6":
                    print("Saliendo del programa.")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")

        elif opcion == "2":
            while True:
                # Menú de proyectos
                print("\n--- Menú de Proyectos ---")
                print("1. Agregar proyecto")
                print("2. Consultar proyecto")
                print("3. Listar todos los proyectos")
                print("4. Eliminar proyecto por nombre")
                print("5. Actualizar tiempos restantes")
                print("6. Salir")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    nombre = input("Nombre del proyecto: ")
                    descripcion = input("Descripción del proyecto: ")
                    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
                    fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
                    estado_actual = input("Estado actual: ")
                    empresa = input("Empresa: ")
                    gerente = input("Gerente: ")
                    equipo = input("Equipo (separado por comas): ").split(", ")
                    proyecto = Proyecto(nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, empresa, gerente, equipo)
                    root = tree.insert(root, proyecto)
                    print("Proyecto agregado exitosamente.")

                elif opcion == "2":
                    gestionProyecto.consulta_proyecto(tree, root)

                elif opcion == "3":
                    print("Lista de proyectos:")
                    tree.list_projects(root)

                elif opcion == "4":
                    nombre = input("Nombre del proyecto a eliminar: ")
                    root = tree.delete(root, nombre)
                    print("Proyecto eliminado exitosamente.")

                elif opcion == "5":
                    print("Actualizando tiempos restantes...")
                    tree.update_remaining_times(root)
                    print("Tiempos restantes actualizados.")

                elif opcion == "6":
                    print("Saliendo del programa.")
                    break

                else:
                    print("Opción no válida. Intente de nuevo.")
                    
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
menu()