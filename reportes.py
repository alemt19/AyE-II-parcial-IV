from datetime import datetime

def consultar_tareas_estado(proyecto, est):
    tareas_filtradas = []
    for i in proyecto.tareas:
        if est == i.estado:
            tareas_filtradas.append(i)
    
    if tareas_filtradas:
        for i in tareas_filtradas:
            print(f"{i.nombre} {i.descripcion} {i.fecha_inicio} {i.fecha_fin} {i.estado} {i.empresa} {i.cliente} {i.porcentaje}")
    else:
        print("No se han encontrado tareas con el estado deseado.")

def filtrado_por_fecha(proyecto):
    tareas_filtradas = []
    print("1. Tareas dentro de un intervalo de fechas")
    print("2. Tareas antes de una fecha")
    print("3. Tareas despues de una fecha")
    x = input("Ingrese la opción de filtrado deseada: ")

    if x == 1:
        fi = input("ingrese la fecha inicial del intervalo en formato YYYY-MM-DD: ")
        fecha_i = datetime.strptime(fi, "%Y-%m-%d")
        ff = input("ingrese la fecha final del intervalo en formato YYYY-MM-DD: ")
        fecha_f = datetime.strptime(ff, "%Y-%m-%d")
        for i in proyecto.tareas:
            if fecha_i < i.fecha.inicio and fecha_f > i.fecha_fin:
                tareas_filtradas.append(i)
    elif x == 2:
        f = input("ingrese una fecha, posterior a las tareas que desea ver, en formato YYYY-MM-DD: ")
        fecha = datetime.strptime(f, "%Y-%m-%d")
        for i in proyecto.tareas:
            if fecha > i.fecha.fin:
                tareas_filtradas.append(i)
    elif x == 3:
        f = input("ingrese una fecha, anterior a las tareas que desea ver, en formato YYYY-MM-DD: ")
        fecha = datetime.strptime(f, "%Y-%m-%d")
        for i in proyecto.tareas:
            if fecha < i.fecha.inicio:
                tareas_filtradas.append(i)

    if tareas_filtradas:
        for i in tareas_filtradas:
            print(f"{i.nombre} {i.descripcion} {i.fecha_inicio} {i.fecha_fin} {i.estado} {i.empresa} {i.cliente} {i.porcentaje}")
    else:
        print("No se han encontrado tareas que cumplan con las condiciones dadas.")
    
def consultar_proyectos(proyectos):
    proyectos_filtrados = []
    print("1. Filtrar por nombre")
    print("2. Filtrar por fecha de inicio")
    print("3. Filtrar por fecha de vencimiento")
    print("4. Filtrar por estado")
    print("5. Filtrar por empresa")
    x = input("Ingrese el número del tipo de filtrado: ")

    if x == 1:
        nombre = input("Ingrese el nombre de los proyectos a filtrar: ")
        for i in proyectos:
            if nombre == i.nombre:
                proyectos_filtrados.append(i)
    elif x == 2:
        f = input("ingrese la fecha de inicio de los proyectos que desea filtrar en formato YYYY-MM-DD: ")
        fecha = datetime.strptime(f, "%Y-%m-%d")
        for i in proyectos:
            if fecha == i.fecha_inicio:
                proyectos_filtrados.append(i)
    elif x == 3:
        f = input("ingrese la fecha de inicio de los proyectos que desea filtrar en formato YYYY-MM-DD: ")
        fecha = datetime.strptime(f, "%Y-%m-%d")
        for i in proyectos:
            if fecha == i.fecha_fin:
                proyectos_filtrados.append(i)
    elif x == 4:
        estado = input("Ingrese el estado de los proyectos que desea filtrar: ")
        for i in proyectos:
            if estado == i.estado:
                proyectos_filtrados.append(i)
    elif x == 5:
        empresa = input("Ingrese la empresa de los proyectos que desea filtrar: ")
        for i in proyectos:
            if empresa == i.empresa:
                proyectos_filtrados.append(i)

    if proyectos_filtrados:
        for i in proyectos_filtrados:
            porcentaje = 0
            completadas = 0
            n = 0
            for j in i.tareas:
                if j.estado == "Completado":
                    completadas += 1
                n += 1
            
            if n == 0:
                porcentaje = 0
            else:
                porcentaje = (completadas/n)*100

            print(f"{i.nombre} {i.descripcion} {i.fecha_inicio} {i.fecha_fin} {i.estado} {i.empresa} {i.gerente} {i.equipo} Porcentaje: {porcentaje}")
    else:
        print("No se han encontrado tareas que cumplan con las condiciones dadas.")

def listar_subtareas(proyecto):

    for i in proyecto.tareas:
            print(f"{i.nombre} {i.descripcion} {i.fecha_inicio} {i.fecha_fin} {i.estado} {i.empresa} {i.cliente} {i.porcentaje}")
            for j in i:
                print(f"---{j.nombre} {j.descripcion} {j.estado}")
            
    