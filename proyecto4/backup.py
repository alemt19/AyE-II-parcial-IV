import json
from lista import ListaEnlazada
from claseEmpresa import Empresa
from gestionTareas import Tarea
from proyecto import Proyecto as pr
from subtarea import Subtarea
from listaEnlazada import LinkedList
import os
import gestion_proyecto_arbolAVL as gestionProyecto
from reportes_proyecto2 import NaryTree
import csv
from gestionSprints import Sprint

def cargar_datos_desde_json():
    proyectos = gestionProyecto.AVLTree()
    config_path = os.path.join("proyecto4", "config.txt")
    # Leer y cargar el archivo de configuración
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
    ruta_proyectos = config["datos"]
    
    # Cargar datos de proyectos
    with open(ruta_proyectos, "r") as archivo:
        datos = json.load(archivo)
        va=0
        for proyecto_data in datos:
            cont = 1
            proyecto = pr(
                proyecto_data["nombre"],
                proyecto_data["descripcion"],
                proyecto_data["fecha_inicio"],
                proyecto_data["fecha_fin"],
                proyecto_data["estado"],
                proyecto_data["empresa"],
                proyecto_data["gerente"],
                proyecto_data["equipo"]
            )
            va=0
            
            proyecto.id = proyecto_data["id"]  # Asigna el ID desde los datos cargados
            for i in proyecto_data["tareas"]:
                if cont == 1:
                    proyecto.tareas = NaryTree(Tarea(
                                        i["nombre"],
                                        i["descripcion"],
                                        i["fecha_inicio"],
                                        i["fecha_fin"],
                                        i["estado"],
                                        i["empresa_cliente"],
                                        i["porcentaje"],
                                        ))
                    cont2 = 1
                    for j in i["subtareas"]:
                        if cont2 == 1:
                            if va<len(proyecto_data["tareas"]):
                                proyecto.tareas.find_node_by_attribute("nombre", i["nombre"]).data.subtareas = NaryTree(
                                    Subtarea(
                                        j["nombre"],
                                        j["descripcion"],
                                        j["estado"]
                                    )
                                )
                        else:
                            if va<len(proyecto_data["tareas"]):
                                subtarea = Subtarea(
                                        j["nombre"],
                                        j["descripcion"],
                                        j["estado"]
                                    )
                                proyecto.tareas.find_node_by_attribute("nombre", i["nombre"]).data.subtareas.add_child_to_node(proyecto.tareas.find_node_by_attribute("nombre", i["nombre"]).data.subtareas.root, subtarea)
                        cont2+=1

                else:
                    proyecto.tareas.add_child_to_node(proyecto.tareas.root, Tarea(
                                        i["nombre"],
                                        i["descripcion"],
                                        i["fecha_inicio"],
                                        i["fecha_fin"],
                                        i["estado"],
                                        i["empresa_cliente"],
                                        i["porcentaje"],
                                        ))
                    for j in i["subtareas"]:
                        if cont2 == 1:
                            if va<len(proyecto_data["tareas"]):
                                proyecto.tareas.find_node_by_attribute("nombre", i["nombre"]).data.subtareas = NaryTree(
                                    Subtarea(
                                        j["nombre"],
                                        j["descripcion"],
                                        j["estado"]
                                    )
                                )
                        else:
                            if va<len(proyecto_data["tareas"]):
                                subtarea = Subtarea(
                                        j["nombre"],
                                        j["descripcion"],
                                        j["estado"]
                                    )
                                proyecto.tareas.find_node_by_attribute("nombre", i["nombre"]).data.subtareas.add_child_to_node(proyecto.tareas.find_node_by_attribute("nombre", i["nombre"]).data.subtareas.root, subtarea)
                                
                        cont2+=1
                va+=1
                cont+=1
            for i in proyecto_data["sprints"]:
                proyecto.sprints.insert2(Sprint(
                    i["nombre"],
                    i["fecha_inicio"],
                    i["fecha_fin"],
                    i["estado"],
                    i["objetivos"],
                    i["equipo"]
                ))

            proyectos.insert2(proyecto)
    
    # Cargar subtareas desde subtareas.json
    # Respaldar datos de proyectos a un archivo
    with open(ruta_proyectos, "w") as respaldo_proyectos:
        json.dump(datos, respaldo_proyectos, indent=4)
    
    return proyectos

# def cargar_sprints_de_json():
#     sprints = LinkedList()
#     config_path = os.path.join("proyecto4", "config.txt")
#     # Leer y cargar el archivo de configuración
#     with open(config_path, "r") as config_file:
#         config = json.load(config_file)
#     ruta_proyectos = config["datos"]
    
#     # Cargar datos de proyectos
#     with open(ruta_proyectos, "r") as archivo:
#         datos = json.load(archivo)
#         for proyecto_data in datos:
#             for sprints in proyecto_data["sprints"]:
#                 for sprint in sprints:
#                     # Clase provisional
#                     nuevo_sprint = Sprint(
#                     sprint["id"],
#                     sprint["nombre"],
#                     sprint["fecha_inicio"],
#                     sprint["fecha_fin"],
#                     sprint["estado"],
#                     sprint["objetivos"],
#                     sprint["equipo"]
#                     )
#                     sprints.append(nuevo_sprint)
#     return sprints


def cargar_datos_desde_csv(proyectosJSON):
    empresas = ListaEnlazada()
    # Leer los datos del archivo CSV datosEmpresa
    with open('proyecto4/datosEmpresas.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row[1] == "nombre":
                empresa = Empresa(
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                )
                empresa.id = int(row[0])
                proyectosAsociados = row[9].split("-")

                for i in proyectosAsociados:
                    empresa.proyectos.insert(proyectosJSON.buscar_proyecto2(proyectosJSON.root, "nombre", i))
                empresas.agregar(empresa)
    return empresas

def guardar_datos_en_json(proyectos):
    data = []
    for p in proyectos:
        if p.__class__.__name__ == "AVLNode":
            proyecto = p.key
        elif p.__class__.__name__ == "Proyecto":
            proyecto = p
        proyecto_data = {
            "id": proyecto.id,
            "nombre": proyecto.nombre,
            "descripcion": proyecto.descripcion,
            "fecha_inicio": proyecto.fecha_inicio.strftime("%Y-%m-%d"),
            "fecha_fin": proyecto.fecha_fin.strftime("%Y-%m-%d"),
            "estado": proyecto.estado_actual,
            "empresa": proyecto.empresa,
            "gerente": proyecto.gerente,
            "equipo": proyecto.equipo,
            "tareas": [],  # Suponiendo que hay una estructura para guardar tareas en Proyecto
            "sprints": []
        }
        if proyecto.sprints.root.__class__.__name__ != "NoneType":
            sprintsLista = proyecto.sprints.inorder_traversal()
            for sprint in sprintsLista:
                sprint_data = {
                    "id": sprint.id,
                    "nombre": sprint.nombre,
                    "fecha_inicio": sprint.fecha_inicio.strftime("%Y-%m-%d"),
                    "fecha_fin": sprint.fecha_fin.strftime("%Y-%m-%d"),
                    "estado": sprint.estado,
                    "objetivos": sprint.objetivos,
                    "equipo": sprint.equipo
                }
                proyecto_data["sprints"].append(sprint_data)
        if proyecto.tareas.root.__class__.__name__ == "NoneType":
            pass
        elif proyecto.tareas.root.data.__class__.__name__ != "NoneType":
            tareas = proyecto.tareas.inorder_traversal(proyecto.tareas.root)
            for tarea in tareas:
                tarea_data = {
                    "id": tarea.id,
                    "nombre": tarea.nombre,
                    "descripcion": tarea.descripcion,
                    "fecha_inicio": tarea.fecha_inicio.strftime("%Y-%m-%d"),
                    "fecha_fin": tarea.fecha_fin.strftime("%Y-%m-%d"),
                    "estado": tarea.estado,
                    "empresa_cliente": tarea.empresa,
                    "porcentaje": tarea.porcentaje,
                    "subtareas" : []
                    # Agregar otros atributos de tarea según sea necesario
                }
                if tarea.subtareas.root.data.__class__.__name__ != "NoneType":
                    subtareas = tarea.subtareas.inorder_traversal(tarea.subtareas.root)
                    if subtareas[0] is not None:
                        for subtarea in subtareas:
                            subtarea_data = {
                            "id": subtarea.id,
                            "nombre": subtarea.nombre,
                            "descripcion": subtarea.descripcion,
                            "estado": subtarea.estado,
                            }
                            tarea_data["subtareas"].append(subtarea_data)
                proyecto_data["tareas"].append(tarea_data)
                
        data.append(proyecto_data)  # Agregamos los datos del proyecto a la lista

    with open("proyecto4\datos.json", 'w') as file:
        json.dump(data, file, indent=4)  # Escribimos los datos en el archivo JSON con formato indentado

def guardar_datos_en_csv(empresas):
    data = [["id", "nombre", "descripcion", "f_creacion", "direccion", "telefono", "correo", "gerente", "equipo_contacto", "proyectos"]]
    for empresa in empresas:
        nombresProyectos = []
        datos = [
            empresa.id,
            empresa.nombre,
            empresa.descripcion,
            empresa.f_creacion.strftime("%Y-%m-%d"),
            empresa.direccion,
            empresa.telefono,
            empresa.correo,
            empresa.gerente,
            empresa.equipo_contacto]
        for proyectoNodo in empresa.proyectos.inorder_traversal():
            nombresProyectos.append(proyectoNodo.key.nombre)
        datos.append("-".join(nombresProyectos))
        data.append(datos)
    with open("proyecto4\datosEmpresas.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)