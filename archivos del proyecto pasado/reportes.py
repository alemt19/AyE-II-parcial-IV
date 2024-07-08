from datetime import datetime

def consultar_tareas_estado(proyectos, est):
    # Funcion que imprime todas las tareas de todos los proyectos si coinciden con el estado
    # Especificado por el usuario
    tareas_filtradas = []
    bandera=0 # Bandera que permite imprimir el nombre del proyecto al que corresponden  las tareas
 
    for i in proyectos:
        # Ciclo para evaluar cada proyecto
        for j in i.tareas:
            # ciclo para evaluar cada tarea del proyecto i
            if est == j.estado:
                # Si coincide el estado dado con el de la tarea se agrega
                if bandera == 0:
                    tareas_filtradas.append(f"{i.nombre}:\n")
                    bandera = 1
                datos = f"{j.nombre}, {j.descripcion}, {j.fecha_inicio}, {j.fecha_fin}, {j.estado}, {j.empresa}, {j.porcentaje}"
                tareas_filtradas.append(datos)
        bandera = 0
    
    if tareas_filtradas:
        # Si se encuentran tareas con el estado dado se imprimen sus datos
        for i in tareas_filtradas:
            print(i)
    else:
        print("No se han encontrado tareas con el estado deseado.")

def filtrado_por_fecha(proyecto):
    # Función para filtrar las tareas de un proyecto, haciendo comparaciones de objetos datetime

    tareas_filtradas = []
    print("1. Tareas dentro de un intervalo de fechas")
    print("2. Tareas antes de una fecha")
    print("3. Tareas despues de una fecha")
    x = int(input("Ingrese la opción de filtrado deseada: "))

    if x == 1:
        # Se ingresan por teclado 2 fechas y se convierten en objetos datetime
        fi = input("ingrese la fecha inicial del intervalo en formato YYYY-MM-DD: ")
        fecha_i = datetime.strptime(fi, "%Y-%m-%d")
        ff = input("ingrese la fecha final del intervalo en formato YYYY-MM-DD: ")
        fecha_f = datetime.strptime(ff, "%Y-%m-%d")

        for i in proyecto.tareas:
            #Ciclo para comparar las fechas del intervalo dado con las fechas de cada tarea del proyecto
            if fecha_i < i.fecha_inicio and fecha_f > i.fecha_fin:
                tareas_filtradas.append(i)
    elif x == 2:
        # Se ingresa por teclado una fecha y se convierte en un objeto datetime
        f = input("ingrese una fecha, posterior a las tareas que desea ver, en formato YYYY-MM-DD: ")
        fecha = datetime.strptime(f, "%Y-%m-%d")
        for i in proyecto.tareas:
            #Ciclo para comparar la fecha dada con la fecha fin de cada tarea del proyecto
            if fecha > i.fecha_fin:
                tareas_filtradas.append(i)
    elif x == 3:
        # Se ingresa por teclado una fecha y se convierte en un objeto datetime
        f = input("ingrese una fecha, anterior a las tareas que desea ver, en formato YYYY-MM-DD: ")
        fecha = datetime.strptime(f, "%Y-%m-%d")
        for i in proyecto.tareas:
            #Ciclo para comparar la fecha dada con la fecha inicio de cada tarea del proyecto
            if fecha < i.fecha_inicio:
                tareas_filtradas.append(i)

    if tareas_filtradas:
        # Si hay tareas que cumplen con los parametros se imprimen con un ciclo for
        for i in tareas_filtradas:
            print(f"{i.nombre}, {i.descripcion}, {i.fecha_inicio}, {i.fecha_fin}, {i.estado}, {i.empresa}, {i.porcentaje}")
    else:
        print("No se han encontrado tareas que cumplan con las condiciones dadas.")
    
def consultar_proyectos(proyectos):
    # Funcion que filtra los proyectos segun un criterio elegido
    proyectos_filtrados = []
    print("1. Filtrar por nombre")
    print("2. Filtrar por fecha de inicio")
    print("3. Filtrar por fecha de vencimiento")
    print("4. Filtrar por estado")
    print("5. Filtrar por empresa")
    x = int(input("Ingrese el número del tipo de filtrado: "))

    # Dependiendo del criterio elegido, se compara este con cada uno de los proyectos
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
            # Si hay proyectos que cumplan con el criterio se calcula el avance a partir de
            # las tareas completadas y las incompletas
            porcentaje = 0
            completadas = 0
            incompletas = 0
            for j in i.tareas:
                if j.estado == "Completado":
                    completadas += 1
                incompletas += 1
            
            if incompletas == 0:
                porcentaje = 0
            else:
                porcentaje = (completadas/incompletas)*100

            print(f"{i.nombre}, {i.descripcion}, {i.fecha_inicio}, {i.fecha_fin}, {i.estado}, {i.empresa}, {i.gerente}, {i.equipo}, Porcentaje: {porcentaje}")
    else:
        print("No se han encontrado tareas que cumplan con las condiciones dadas.")

def listar_subtareas(proyecto):
    # Funcion que itera las tareas de un proyecto e imprime su informacion
    # En cada iteracion se iteran las subtareas para imprimirlas
    for i in proyecto.tareas:
        print(f"{i.nombre}, {i.descripcion}, {i.fecha_inicio}, {i.fecha_fin}, {i.estado}, {i.empresa}, {i.porcentaje}")
        for j in i.subtareas:
            print(f"---{j.nombre} {j.descripcion} {j.estado}")
            
    