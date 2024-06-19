from gestion_proyecto import Gestion
import backup as bu
from modificar_json import guardar_datos_en_json
gestion = Gestion()
for i in bu.cargar_datos_desde_json():
    gestion.proyectos.append(i)

gestion.menu()
guardar_datos_en_json(gestion.proyectos)