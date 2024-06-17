from gestion_proyecto import Gestion
import backup as bu
gestion = Gestion()
for i in bu.cargar_datos_desde_json():
    gestion.proyectos.append(i)

gestion.menu()