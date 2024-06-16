import json
from datetime import datetime


def cargar_datos_desde_json(nombre_archivo):
    proyectos = []
    
    # Cargar rutas desde el archivo de configuración
    with open("config.txt", "r") as config_file:
        config = json.load(config_file)
        ruta_proyectos = config["datos"]
        ruta_subtareas = config["subtareas"]
    
    # Cargar datos de proyectos
    with open(ruta_proyectos, "r") as archivo:
        datos = json.load(archivo)
        for proyecto_data in datos:
            proyecto = proyecto(
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
                tarea_obj = tarea(
                    tarea["id"],
                    tarea["nombre"],
                    "",  # Cliente (si es necesario añadirlo)
                    tarea["descripcion"],
                    datetime.strptime(tarea["fecha_inicio"], "%Y-%m-%d"),
                    datetime.strptime(tarea["fecha_vencimiento"], "%Y-%m-%d"),
                    tarea["estado"],
                    0  # Avance (si es necesario añadirlo)
                )
                
                for subtarea_data in tarea.get("subtareas", []):
                    subtarea_obj = Subtarea( # type: ignore
                        subtarea_data["id"],
                        subtarea_data["nombre"],
                    )
                    tarea_obj.agregar_subtarea(subtarea_obj)
                
                proyecto.agregar_tarea(tarea_obj)
    
    # Respaldar datos de proyectos a un archivo
    with open(ruta_proyectos, "w") as respaldo_proyectos:
        json.dump(datos, respaldo_proyectos, indent=4)
    
    return proyectos







