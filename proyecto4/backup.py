import json
from datetime import datetime
from gestionTareas import Tarea
from proyecto import Proyecto as pr
from subtarea import Subtarea
import os
import gestion_proyecto_arbolAVL as gestionProyecto
from reportes_proyecto2 import NaryTree

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
                proyecto_data["estado_actual"],
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







