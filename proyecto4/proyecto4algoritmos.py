import cola as co 
import pila as pi
import lista as lst
from datetime import datetime
#clase proyecto
class Proyecto: 
    id=0
    def __init__(self,nombre,descripcion,fecha_inicio,fecha_fin,estado,empresa,gerente,equipo):
        Proyecto.id+=1
        self.id=Proyecto.id
        self.nombre=nombre
        self.descripcion=descripcion
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        self.estado=estado
        self.empresa=empresa
        self.gerente=gerente
        self.equipo=equipo
        self.tareas=pi.Pila()
#clase gestion que contiene los menus de gestion de proyectos
class Gestion:
    def __init__(self):
        #cola que almacena los proyectos que vayamos agregando
        self.proyecto=co.Cola()
    def menu(self):
        x=1
        #ciclo while que contiene al menu de gestion de proyectos
        while x!=0:
            print("-presione 1 para crear un proyecto")
            print("-presione 2 para modificar un proyecto")
            print("-presione 3 para consultar un proyecto")
            print("-presione 4 para eliminar un proyecto")
            print("-presione 5 para listar los proyectos actuales")
            print("-presione 0 para salir del programa")
            x=int(input("ingrese una opcion: "))
            print("------------------------")
            if x==1:
                #si x es uno creamos un nuevo objeto proyecto
                nom=input("ingrese el nombre del proyecto: ")
                desc=input("ingrese la descripcion del proyecto: ")
                fi=input("ingrese la fecha de inicio en formato YYYY-MM-DD: ")
                fid=datetime.strptime(fi, "%Y-%m-%d")
                ff=input("ingrese la fecha final del proyecto en formato YYYY-MM-DD: ")
                ffd=datetime.strptime(ff,"%Y-%m-%d")
                estado=input("ingrese el estado de el proyecto: ")
                empresa=input("ingrese la empresa del proyecto: ")
                gerente=input("ingrese el gerente del proyecto: ")
                equipo=input("ingrese el equipo del proyecto: ")
                proyecto=Proyecto(nom,desc,fid,ffd,estado,empresa,gerente,equipo)
                self.proyecto.agregar(proyecto)
                print("proyecto agregado correctamente!")
                print("---------------------------")
            elif x==2:
                #si x es dos desplegamos un menu que nos dice que queremos modificar del objeto proyecto
                #la variable m guarda el nombre del proyecto que vamos a modificar
                m=input("ingrese el nombre del proyecto a modificar: ")
                #si la variable m es igual al nombre de un proyecto significa que vamos a modificar dicho proyecto
                if self.proyecto.buscar_nombre(m) == True:
                    print("-presione 1 para modificar el nombre")
                    print("-presione 2 para modificar la descripcion")
                    print("-presione 3 para modificar la fecha de inicio")
                    print("-presione 4 para modificar la fecha de vencimiento")
                    print("-presione 5 para modificar el estado")
                    print("-presione 6 para modificar el gerente")
                    print("-presione 7 para modificar la empresa")
                    print("-presione 8 para modificar el equipo")
                    xm=int(input("ingrese una opcion: "))
                    print("-------------------------------")
                    #actualizamos el objeto proyecto respecto a la opcion que hayamos escogido
                    if xm==1:
                        nuevo_nombre=input("ingrese el nuevo nombre del proyecto: ")
                        self.proyecto.devolver_objeto(m).nombre=nuevo_nombre
                        print("proyecto modificado exitosamente!")
                    elif xm==2:
                        nueva_desc=input("ingrese la nueva descripcion del proyecto: ")
                        self.proyecto.devolver_objeto(m).descripcion=nueva_desc
                        print("proyecto modificado exitosamente!")
                    elif xm==3:
                        nueva_fi=input("ingrese la nueva fecha de inicio del proyecto: ")
                        self.proyecto.devolver_objeto(m).fecha_inicio=nueva_fi
                        print("proyecto modificado exitosamente!")
                    elif xm==4:
                        nueva_ff=input("ingrese la nueva fecha de vencimiento del proyecto: ")
                        self.proyecto.devolver_objeto(m).fecha_fin=nueva_ff
                        print("proyecto modificado exitosamente!")
                    elif xm == 5: 
                        nueva_ff=input("ingrese el nuevo estado del proyecto: ")
                        self.proyecto.devolver_objeto(m).fecha_fin=nueva_ff
                        print("proyecto modificado exitosamente!")
                    elif xm==6:
                        nuevo_gerente=input("ingrese el nuevo gerente del proyecto: ")
                        self.proyecto.devolver_objeto(m).gerente=nuevo_gerente
                        print("proyecto modificado exitosamente!")
                    elif xm==7:
                        nueva_empresa=input("ingrese la nueva empresa del proyecto: ")
                        self.proyecto.devolver_objeto(m).empresa=nueva_empresa
                        print("proyecto modificado exitosamente!")
                    elif xm==8:
                        nuevo_equipo=input("ingrese el nuevo equipo del proyecto: ")
                        self.proyecto.devolver_objeto(m).equipo=nuevo_equipo
                        print("proyecto modificado exitosamente!")
                    else:
                        print("error, opcion no valida")
                else:
                    print("proyecto no encontrado")
                
            elif x == 3:
                m = input("ingrese el nombre del proyecto a consultar: ")
                print("-------------------------------")
                if self.proyecto.buscar_nombre(m) == True:
                    print(f"id: {self.proyecto.devolver_objeto(m).id}")
                    print(f"nombre: {self.proyecto.devolver_objeto(m).nombre}")
                    print(f"descripcion: {self.proyecto.devolver_objeto(m).descripcion}")
                    print(f"fecha de inicio: {self.proyecto.devolver_objeto(m).fecha_inicio}")
                    print(f"fecha de vencimiento: {self.proyecto.devolver_objeto(m).fecha_fin}")
                    print(f"estado: {self.proyecto.devolver_objeto(m).estado}")
                    print(f"empresa: {self.proyecto.devolver_objeto(m).empresa}")
                    print(f"gerente: {self.proyecto.devolver_objeto(m).gerente}")
                    print(f"equipo: {self.proyecto.devolver_objeto(m).equipo}")
                print("------------------------------")
            elif x == 4:
                #si x es igual a 4 se elimina un proyecto basandonos en su nombre
                m=input("ingrese el nombre del proyecto a eliminar: ")
                if self.proyecto.buscar_nombre(m) == True:
                    self.proyecto.eliminar(m)
                    print("proyecto eliminado correctamente!")
            elif x == 5:
                #si x es igual a 5 listamos los proyectos actuales
                self.proyecto.recorrer()


        print("fin del programa")
            
gestion = Gestion()
gestion.menu()
                    


                

                

    

        

        
    
