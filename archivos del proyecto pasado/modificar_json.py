from datetime import datetime
import json


def cargar_datos_desde_json(self):
    try:
        with open(self.file_path, 'r') as file:
            data = json.load(file)  # Cargamos los datos del archivo JSON
            proyectos = []
            for proyecto_data in data:
                # Creamos instancias de Proyecto a partir de los datos del JSON
                proyecto = proyecto(
                    proyecto_data["id"],
                    proyecto_data["nombre"],
                    proyecto_data["descripcion"],
                    datetime.strptime(proyecto_data["fecha_inicio"], "%Y-%m-%d"),
                    datetime.strptime(proyecto_data["fecha_vencimiento"], "%Y-%m-%d"),
                    proyecto_data["estado"],
                    proyecto_data["empresa"],
                    proyecto_data["gerente"],
                    proyecto_data["equipo"]
                )
                proyectos.append(proyecto)  # Agregamos el proyecto a la lista
            return proyectos  # Retornamos la lista de proyectos
    except FileNotFoundError:
        print("Archivo no encontrado. Iniciando con lista vacía.")
        return []  # Si no se encuentra el archivo, retornamos una lista vacía

def guardar_datos_en_json(proyectos):
    data = []
    for proyecto in proyectos:
        proyecto_data = {
            "id": proyecto.id,
            "nombre": proyecto.nombre,
            "descripcion": proyecto.descripcion,
            "fecha_inicio": proyecto.fecha_inicio.strftime("%Y-%m-%d"),
            "fecha_vencimiento": proyecto.fecha_fin.strftime("%Y-%m-%d"),
            "estado": proyecto.estado,
            "empresa": proyecto.empresa,
            "gerente": proyecto.gerente,
            "equipo": proyecto.equipo,
            "tareas": []  # Suponiendo que hay una estructura para guardar tareas en Proyecto
        }
        for tarea in proyecto.tareas:
            tarea_data = {
                "id": tarea.id,
                "nombre": tarea.nombre,
                "descripcion": tarea.descripcion,
                "fecha_inicio": tarea.fecha_inicio.strftime("%Y-%m-%d"),
                "fecha_vencimiento": tarea.fecha_fin.strftime("%Y-%m-%d"),
                "estado": tarea.estado,
                "empresa_cliente": tarea.empresa,
                "porcentaje": tarea.porcentaje,
                "subtareas" : []
                # Agregar otros atributos de tarea según sea necesario
            }
            for subtarea in tarea.subtareas:
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

def filtrar_tareas_por_rango(self, fecha_inicio, fecha_fin):
    tareas_filtradas = []
    for proyecto in self.proyectos:
        for tarea in proyecto.tareas:
            if fecha_inicio <= tarea.fecha_inicio <= fecha_fin:
                tareas_filtradas.append(tarea)  # Filtramos las tareas por rango de fechas
    return tareas_filtradas  # Retornamos la lista de tareas filtradas

def filtrar_proyectos_por_rango(self, fecha_inicio, fecha_fin):
    proyectos_filtrados = []
    for proyecto in self.proyectos:
        if fecha_inicio <= proyecto.fecha_inicio <= fecha_fin:
            proyectos_filtrados.append(proyecto)  # Filtramos los proyectos por rango de fechas
    return proyectos_filtrados  # Retornamos la lista de proyectos filtrados

def filtrar_por_id(self):
    id_proyecto = int(input("Ingrese el id del proyecto: "))
    for proyecto in self.proyectos:
        if proyecto.id == id_proyecto:
            return proyecto  # Retornamos el proyecto que coincide con el ID ingresado
    return None  # Si no se encuentra el proyecto, retornamos None

def agregar_proyecto(self):
    id_proyecto = int(input("Ingrese el id del proyecto: "))
    nombre = input("Ingrese el nombre del proyecto: ")
    descripcion = input("Ingrese la descripción del proyecto: ")
    fecha_inicio = datetime.strptime(input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): "), "%Y-%m-%d")
    fecha_vencimiento = datetime.strptime(input("Ingrese la fecha de vencimiento del proyecto (YYYY-MM-DD): "), "%Y-%m-%d")
    estado = input("Ingrese el estado del proyecto: ")
    empresa = input("Ingrese la empresa del proyecto: ")
    gerente = input("Ingrese el gerente del proyecto: ")
    equipo = input("Ingrese el equipo del proyecto: ")

    proyecto = proyecto(id_proyecto, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado, empresa, gerente, equipo)
    self.proyectos.append(proyecto)  # Agregamos el nuevo proyecto a la lista
    self.guardar_datos_en_json()  # Guardamos los cambios en el archivo JSON

def eliminar_proyecto(self):
    print("Proyectos:")
    for proyecto in self.proyectos:
        print(proyecto.nombre)
    nombre_proyecto = input("¿Cuál proyecto desea eliminar? Ingrese el nombre: ")
    for proyecto in self.proyectos:
        if proyecto.nombre == nombre_proyecto:
            self.proyectos.remove(proyecto)  # Eliminamos el proyecto de la lista
            self.guardar_datos_en_json()  # Guardamos los cambios en el archivo JSON
            print(f"Proyecto {nombre_proyecto} eliminado correctamente.")
            return
    print(f"No se encontró ningún proyecto con el nombre {nombre_proyecto}.")

def mostrar_proyectos(self, proyectos=None):
    if proyectos is None:
        proyectos = self.proyectos
    
    for proyecto in proyectos:
        print(f"Proyecto: {proyecto.nombre}")
        for tarea in proyecto.tareas:
            print(f"\tTarea: {tarea.nombre}")
            if hasattr(tarea, 'subtareas') and tarea.subtareas:
                for subtarea in tarea.subtareas:
                    print(f"\t\tSubtarea: {subtarea.nombre}")
            else:
                print("\t\tNo hay subtareas")

