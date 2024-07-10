import gestion_proyecto_arbolAVL as gestionProyectos
import gestionEmpresas
import gestionTareas
from backup import cargar_datos_desde_json
from backup import cargar_datos_desde_csv

def menuPrincipal():
    tree = cargar_datos_desde_json()
    empresas = cargar_datos_desde_csv(tree)

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
                    gestionEmpresas.consultar_empresa(empresas)
                elif opcion == "3":
                    gestionEmpresas.listar_empresas(empresas)
                elif opcion == "4":
                    gestionEmpresas.eliminar_empresa(empresas)
                elif opcion == "5":
                    gestionEmpresas.modificar_empresa(empresas)
                elif opcion == "6":
                    print("Saliendo del programa.")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")

        elif opcion == "2":
            # Menú de proyectos
            idEmpresa = input("Ingrese el ID de la empresa de la cual desea gestionar los proyectos")
            proyectos = (empresas.obtener(idEmpresa)).proyectos
            gestionProyectos.menu(proyectos)

        elif opcion == "3":
            nombre = input("Ingrese el nombre del proyecto del cual quiere gestionar sus tareas: ")
            result = tree.buscar_proyecto( 'nombre', nombre)
            gestionTareas.menu(result.tareas)

        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
menuPrincipal()