import json
from lista import ListaEnlazada
from claseEmpresa import Empresa
from gestionTareas import Tarea
from proyecto import Proyecto as pr
from subtarea import Subtarea
import os
import gestion_proyecto_arbolAVL as gestionProyecto
from reportes_proyecto2 import NaryTree
import csv

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
                    for j in i["subtareas"]:
                        if va<len(proyecto_data["tareas"]):

                            proyecto.tareas.find_node_by_attribute("nombre", i["nombre"]).data.subtareas = NaryTree(
                                Subtarea(
                                    j["nombre"],
                                    j["descripcion"],
                                    j["estado"]
                                )
                            )
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
                        if va<len(proyecto_data["tareas"]):

                            proyecto.tareas.find_node_by_attribute("nombre", i["nombre"]).data.subtareas.add_child_to_node(
                                proyecto.tareas.find_node_by_attribute("nombre", i["nombre"]).data.subtareas.root,
                                Subtarea(
                                    j["nombre"],
                                    j["descripcion"],
                                    j["estado"]
                                )
                            )
                va+=1
                cont+=1
            proyectos.insert(proyecto)
    
    # Cargar subtareas desde subtareas.json
    # Respaldar datos de proyectos a un archivo
    with open(ruta_proyectos, "w") as respaldo_proyectos:
        json.dump(datos, respaldo_proyectos, indent=4)
    
    return proyectos

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
                    empresa.proyectos.insert(proyectosJSON.buscar_proyecto(proyectosJSON.root, "nombre", i))
                empresas.agregar(empresa)
    return empresas

def guardar_datos_en_json(proyectos):
    data = []
    for proyecto in proyectos:
        proyecto_data = {
            "id": proyecto.key.id,
            "nombre": proyecto.key.nombre,
            "descripcion": proyecto.key.descripcion,
            "fecha_inicio": proyecto.key.fecha_inicio.strftime("%Y-%m-%d"),
            "fecha_fin": proyecto.key.fecha_fin.strftime("%Y-%m-%d"),
            "estado": proyecto.key.estado_actual,
            "empresa": proyecto.key.empresa,
            "gerente": proyecto.key.gerente,
            "equipo": proyecto.key.equipo,
            "tareas": []  # Suponiendo que hay una estructura para guardar tareas en Proyecto
        }
        tareas = proyecto.key.tareas.inorder_traversal(proyecto.key.tareas.root)
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