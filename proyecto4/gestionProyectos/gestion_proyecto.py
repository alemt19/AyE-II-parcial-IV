from datetime import datetime
import cola as co
import proyecto as pr

class Gestion:
    def __init__(self):
        self.proyecto = co.Cola()
    
    def menu(self):
        x = 1
        while x != 0:
            print("-presione 1 para crear un proyecto")
            print("-presione 2 para modificar un proyecto")
            print("-presione 3 para consultar un proyecto")
            print("-presione 4 para eliminar un proyecto")
            print("-presione 5 para listar los proyectos actuales")
            print("-presione 0 para salir del programa")
            x = int(input("ingrese una opcion: "))
            print("------------------------")
            if x == 1:
                self.crear_proyecto()
            elif x == 2:
                self.modificar_proyecto()
            elif x == 3:
                self.consultar_proyecto()
            elif x == 4:
                self.eliminar_proyecto()
            elif x == 5:
                self.listar_proyectos()

        print("fin del programa")
    
    def crear_proyecto(self):
        nom = input("ingrese el nombre del proyecto: ")
        desc = input("ingrese la descripcion del proyecto: ")
        fi = input("ingrese la fecha de inicio en formato YYYY-MM-DD: ")
        fid = datetime.strptime(fi, "%Y-%m-%d")
        ff = input("ingrese la fecha final del proyecto en formato YYYY-MM-DD: ")
        ffd = datetime.strptime(ff, "%Y-%m-%d")
        estado = input("ingrese el estado de el proyecto: ")
        empresa = input("ingrese la empresa del proyecto: ")
        gerente = input("ingrese el gerente del proyecto: ")
        equipo = input("ingrese el equipo del proyecto: ")
        proyecto = pr.Proyecto(nom, desc, fid, ffd, estado, empresa, gerente, equipo)
        self.proyecto.agregar(proyecto)
        print("proyecto agregado correctamente!")
        print("---------------------------")
    
    def modificar_proyecto(self):
        m = input("ingrese el nombre del proyecto a modificar: ")
        if self.proyecto.buscar_nombre(m):
            print("-presione 1 para modificar el nombre")
            print("-presione 2 para modificar la descripcion")
            print("-presione 3 para modificar la fecha de inicio")
            print("-presione 4 para modificar la fecha de vencimiento")
            print("-presione 5 para modificar el estado")
            print("-presione 6 para modificar el gerente")
            print("-presione 7 para modificar la empresa")
            print("-presione 8 para modificar el equipo")
            xm = int(input("ingrese una opcion: "))
            print("-------------------------------")
            proyecto = self.proyecto.devolver_objeto(m)
            if xm == 1:
                nuevo_nombre = input("ingrese el nuevo nombre del proyecto: ")
                proyecto.nombre = nuevo_nombre
                print("proyecto modificado exitosamente!")
            elif xm == 2:
                nueva_desc = input("ingrese la nueva descripcion del proyecto: ")
                proyecto.descripcion = nueva_desc
                print("proyecto modificado exitosamente!")
            elif xm == 3:
                nueva_fi = input("ingrese la nueva fecha de inicio del proyecto en formato YYYY-MM-DD: ")
                proyecto.fecha_inicio = datetime.strptime(nueva_fi, "%Y-%m-%d")
                print("proyecto modificado exitosamente!")
            elif xm == 4:
                nueva_ff = input("ingrese la nueva fecha de vencimiento del proyecto en formato YYYY-MM-DD: ")
                proyecto.fecha_fin = datetime.strptime(nueva_ff, "%Y-%m-%d")
                print("proyecto modificado exitosamente!")
            elif xm == 5:
                nuevo_estado = input("ingrese el nuevo estado del proyecto: ")
                proyecto.estado = nuevo_estado
                print("proyecto modificado exitosamente!")
            elif xm == 6:
                nuevo_gerente = input("ingrese el nuevo gerente del proyecto: ")
                proyecto.gerente = nuevo_gerente
                print("proyecto modificado exitosamente!")
            elif xm == 7:
                nueva_empresa = input("ingrese la nueva empresa del proyecto: ")
                proyecto.empresa = nueva_empresa
                print("proyecto modificado exitosamente!")
            elif xm == 8:
                nuevo_equipo = input("ingrese el nuevo equipo del proyecto: ")
                proyecto.equipo = nuevo_equipo
                print("proyecto modificado exitosamente!")
            else:
                print("error, opcion no valida")
        else:
            print("proyecto no encontrado")
    
    def consultar_proyecto(self):
        m = input("ingrese el nombre del proyecto a consultar: ")
        print("-------------------------------")
        if self.proyecto.buscar_nombre(m):
            proyecto = self.proyecto.devolver_objeto(m)
            print(f"id: {proyecto.id}")
            print(f"nombre: {proyecto.nombre}")
            print(f"descripcion: {proyecto.descripcion}")
            print(f"fecha de inicio: {proyecto.fecha_inicio}")
            print(f"fecha de vencimiento: {proyecto.fecha_fin}")
            print(f"estado: {proyecto.estado}")
            print(f"empresa: {proyecto.empresa}")
            print(f"gerente: {proyecto.gerente}")
            print(f"equipo: {proyecto.equipo}")
        print("------------------------------")
    
    def eliminar_proyecto(self):
        m = input("ingrese el nombre del proyecto a eliminar: ")
        if self.proyecto.buscar_nombre(m):
            self.proyecto.eliminar(m)
            print("proyecto eliminado correctamente!")
    
    def listar_proyectos(self):
        self.proyecto.recorrer()
