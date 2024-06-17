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
    ruta_subtareas = config["subtareas"]
    
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
            
            proyectos.append(proyecto)
    
    # Cargar subtareas desde subtareas.json
    with open(ruta_subtareas, "r") as subtareas_archivo:
        subtareas_datos = json.load(subtareas_archivo)
        for proyecto in proyectos:
            proyecto_id = proyecto.id
            for tarea in subtareas_datos.get(str(proyecto_id), []):
                tarea_obj = tr.Tareas(
                    tarea["id"],
                    tarea["nombre"],
                    "",  # Cliente (si es necesario añadirlo)
                    tarea["descripcion"],
                    datetime.strptime("1999-12-12", "%Y-%m-%d"),
                    datetime.strptime(tarea["fecha_vencimiento"], "%Y-%m-%d"),
                    "completado",
                    0  # Avance (si es necesario añadirlo)
                )
                
                for subtarea_data in tarea.get("subtareas", []):
                    subtarea_obj = Subtarea( # type: ignore
                        subtarea_data["id"],
                        subtarea_data["nombre"],
                    )
                    tarea_obj.agregar_subtarea(subtarea_obj)
                
                proyecto.tareas.append(tarea_obj)
    
    # Respaldar datos de proyectos a un archivo
    with open(ruta_proyectos, "w") as respaldo_proyectos:
        json.dump(datos, respaldo_proyectos, indent=4)
    
    return proyectos







