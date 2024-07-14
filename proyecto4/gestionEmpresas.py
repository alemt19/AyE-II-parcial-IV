from datetime import datetime
from claseEmpresa import Empresa

def crear_empresa(empresas):
    try:
        nombre = input("Ingrese el nombre: ")
        descripcion = input("Ingrese la descripción: ")
        creacion = input("Ingrese la fecha de creación en formato YYYY-MM-DD: ")
        direccion = input("Ingrese la dirección: ")
        telefono = input("Ingrese el telefono: ")
        correo = input("Ingrese el correo: ")
        gerente = input("Ingrese el nombre del gerente: ")
        contacto = input("Ingrese el contacto: ")

        if(
            len(creacion.split("-")) == 3
        ):
            empresas.agregar(Empresa(nombre, descripcion, creacion, direccion, telefono, correo, gerente, contacto)) 
            print("Empresa agregada correctamente.")      
        else:
            print("Fecha invalida")
    except Exception as e:
        print("Se han ingresado datos no válidos, intente nuevamente.", e)

def modificar_empresa(empresas):
    i = int(input("Ingrese el id de la empresa que desea modificar: "))
    empresa = empresas.obtener(i)
    print("1. Cambiar nombre")
    print("2. Cambiar descripción")
    print("3. Cambiar fecha de creación")
    print("4. Cambiar dirección")
    print("5. Cambiar correo")
    print("6. Cambiar teléfono")
    print("7. Cambiar nombre del gerente")
    print("8. Cambiar contacto")
    x = input("Ingrese el número del atributo a cambiar: ")

    if x == "1":
        empresa.nombre = input("Ingrese el nuevo nombre: ")
        print("Atributo modificado exitosamente")
    elif x == "2":
        empresa.descripcion = input("Ingrese la nueva descripción: ")
        print("Atributo modificado exitosamente")
    elif x == "3":
        creacion = input("Ingrese la nueva fecha de creación en formato YYYY-MM-DD: : ")
        empresa.f_creacion = datetime.strptime(creacion, "%Y-%m-%d")
        print("Atributo modificado exitosamente")
    elif x == "4":
        empresa.direccion = input("Ingrese la nueva dirección: ")
        print("Atributo modificado exitosamente")
    elif x == "5":
        empresa.correo = input("Ingrese el nuevo correo: ")
        print("Atributo modificado exitosamente")
    elif x == "6":
        empresa.telefono = input("Ingrese el nuevo teléfono: ")
        print("Atributo modificado exitosamente")
    elif x == "7":
        empresa.gerente = input("Ingrese el nuevo nombre del gerente: ")
        print("Atributo modificado exitosamente")
    elif x == "8":
        empresa.contacto = input("Ingrese el nuevo contacto: ")
        print("Atributo modificado exitosamente")

def eliminar_empresa(empresas):
    i = int(input("Ingrese el ID de la empresa que desea eliminar: "))
    empresa = empresas.obtener(i-1)
    if (empresas.eliminar(empresa)):
        print("Empresa eliminada exitosamente")
    else:
        print("No se ha encontrado una empresa")

def consultar_empresa(empresas):
    i = int(input("Ingrese el ID de la empresa que desea consultar: "))
    
    if (empresas.obtener(i-1)):
        empresa = empresas.obtener(i-1)
        print(f"{empresa.nombre}, {empresa.descripcion}, {empresa.f_creacion}, {empresa.direccion}, {empresa.correo}, {empresa.telefono}, {empresa.gerente}, {empresa.equipo_contacto}")
    else:
        print("No se ha encontrado una empresa con el ID dado")

def listar_empresas(empresas):
    print("Lista de empresas cliente: ")
    for i in range(0, empresas.longitud):
        print(f"{empresas.obtener(i).nombre}, {empresas.obtener(i).descripcion}, {empresas.obtener(i).f_creacion}, {empresas.obtener(i).direccion}, {empresas.obtener(i).correo}, {empresas.obtener(i).telefono}, {empresas.obtener(i).gerente}, {empresas.obtener(i).equipo_contacto}")
        