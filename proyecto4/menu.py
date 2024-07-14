import gestion_proyecto_arbolAVL as gestionProyectos
import gestionEmpresas
import gestionTareas
from backup import cargar_datos_desde_json
from backup import cargar_datos_desde_csv
from backup import guardar_datos_en_json
from backup import guardar_datos_en_csv

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
        opcion = str(input("Seleccione una opción: "))

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
                opcion = str(input("Seleccione una opción: "))
                
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
                    print("Opción no válida. Intente de nuevosfsd.")

        elif opcion == "2":
            # Menú de proyectos
            idEmpresa = int(input("Ingrese el ID de la empresa de la cual desea gestionar los proyectos: "))
            proyectos = (empresas.obtener(idEmpresa-1)).proyectos
            gestionProyectos.menu(proyectos)

        elif opcion == "3":
            idEmpresa = int(input("Ingrese el ID de la empresa de la cual desea gestionar los proyectos: "))
            empresa = empresas.obtener(idEmpresa-1)
            proyectos = empresa.proyectos
            nombre = input("Ingrese el nombre del proyecto del cual quiere gestionar sus tareas: ")
            proyecto = proyectos.buscar_proyecto(proyectos.root, 'nombre', nombre)
            if proyecto is None:
                print("no se encontro el proyecto")
            else:
                gestionTareas.menu(proyecto.key.key.tareas)

        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    
    proyectosTotales = []
    for i in range(0, empresas.longitud):
        proyectos = empresas.obtener(i).proyectos.inorder_traversal()
        for j in proyectos:
            proyectosTotales.append(j)
    guardar_datos_en_json(proyectosTotales)
    guardar_datos_en_csv(empresas.obtener_nodos())
menuPrincipal()