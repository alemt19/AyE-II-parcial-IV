import json
from datetime import datetime
import tareas as tr
from proyecto import Proyecto as pr
import os

def cargar_datos_desde_json():
    proyectos = []
    config_path = os.path.join("proyecto4", "config.txt")
    # Leer y cargar el archivo de configuración
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
    ruta_proyectos = config["datos"]
    
    # Cargar datos de proyectos
    with open(ruta_proyectos, "r") as archivo:
        datos = json.load(archivo)
        for proyecto_data in datos:
            proyecto = pr(
                proyecto_data["nombre"],
                proyecto_data["descripcion"],
                datetime.strptime(proyecto_data["fecha_inicio"], "%Y-%m-%d"),
                datetime.strptime(proyecto_data["fecha_vencimiento"], "%Y-%m-%d"),
                proyecto_data["estado"],
                proyecto_data["empresa"],
                proyecto_data["gerente"],
                proyecto_data["equipo"]
            )
            
            proyecto.id = proyecto_data["id"]  # Asigna el ID desde los datos cargados
            for i in proyecto_data["tareas"]:
                proyecto.tareas.append(tr.Tareas(i["id"],
                                       i["nombre"],
                                       i["descripcion"],
                                       i["fecha_inicio"],
                                       i["fecha_vencimiento"],
                                       i["estado"],
                                       i["empresa"],
                                       i["cliente"],
                                       i["porcentaje"],
                                       i["subtareas"]))
            proyectos.append(proyecto)
    
    # Cargar subtareas desde subtareas.json
    # Respaldar datos de proyectos a un archivo
    with open(ruta_proyectos, "w") as respaldo_proyectos:
        json.dump(datos, respaldo_proyectos, indent=4)
    
    return proyectos







