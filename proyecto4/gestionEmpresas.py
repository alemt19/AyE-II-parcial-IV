from datetime import datetime
from claseEmpresa import Empresa

class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.longitud = 0

    def __len__(self):
        return self.longitud
    
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.valor
            actual = actual.siguiente

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1

    def eliminar(self, valor):
        if self.cabeza is None:
            return False
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1
            return True
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente
                self.longitud -= 1
                return True
            actual = actual.siguiente
        return False
    
    def insertar(self, indice, valor):
        if indice < 0 or indice > self.longitud:
            raise IndexError("Índice fuera de rango")
        nuevo_nodo = Nodo(valor)
        if indice == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            for i in range(indice - 1):
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1

    def obtener(self, indice):
        if indice < 0 or indice >= self.longitud:
            raise IndexError("Índice fuera de rango")
        actual = self.cabeza
        for i in range(indice):
            actual = actual.siguiente
        return actual.valor
    
    def index(self, valor):
        actual = self.cabeza
        indice = 0
        while actual:
            if actual.valor == valor:
                return indice
            actual = actual.siguiente
            indice += 1
        raise ValueError("{} no está en la lista".format(valor))
    
    def pop(self, indice=None):
        if indice is None:
            indice = self.longitud - 1
        if indice < 0 or indice >= self.longitud:
            raise IndexError("Índice fuera de rango")
        if indice == 0:
            valor = self.cabeza.valor
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1
            return valor
        actual = self.cabeza
        for i in range(indice - 1):
            actual = actual.siguiente
        valor = actual.siguiente.valor
        actual.siguiente = actual.siguiente.siguiente
        self.longitud -= 1
        return valor

def crear_empresa(empresas):
    nombre = input("Ingrese el nombre: ")
    descripcion = input("Ingrese la descripción: ")
    creacion = input("Ingrese la fecha de creación en formato YYYY-MM-DD: ")
    fecha = datetime.strptime(creacion, "%Y-%m-%d")
    direccion = input("Ingrese la dirección: ")
    telefono = input("Ingrese el telefono: ")
    correo = input("Ingrese el correo: ")
    gerente = input("Ingrese el nombre del gerente: ")
    contacto = input("Ingrese el contacto: ")

    if(
        type(nombre) == str and
        type(descripcion) == str and
        isinstance(fecha, datetime.datetime) and
        type(direccion) == str and
        type(telefono) == str and
        type(correo) == str and
        type(gerente) == str and
        type(contacto) == str
    ):
        empresas.agregar(Empresa(nombre, descripcion, creacion, direccion, telefono, correo, gerente, contacto)) 
        print("Empresa agregada correctamente.")      
    else:
        print("Error al procesar los datos de la nueva empresa")

def modificar_empresa(empresas):
    i = int(input("Ingrese el id de la empresa que desea modificar"))
    empresa = empresas.obtener(i)
    print("1. Cambiar nombre")
    print("2. Cambiar descripción")
    print("3. Cambiar fecha de creación")
    print("4. Cambiar dirección")
    print("5. Cambiar correo")
    print("6. Cambiar teléfono")
    print("7. Cambiar nombre del gerente")
    print("8. Cambiar contacto")
    x = input("Ingrese el número del atributo a cambiar")

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
    empresa = empresas.obtener(i)
    if (empresas.eliminar(empresa)):
        print("Empresa eliminada exitosamente")
    else:
        print("No se ha encontrado una empresa")

def consultar_empresa(empresas):
    i = int(input("Ingrese el ID de la empresa que desea consultar: "))
    
    if (empresas.obtener(i)):
        empresa = empresas.obtener(i)
        print(f"{empresa.nombre}, {empresa.descripcion}, {empresa.f_creacion}, {empresa.direccion}, {empresa.correo}, {empresa.telefono}, {empresa.gerente}, {empresa.contacto}")
    else:
        print("No se ha encontrado una empresa con el ID dado")

def listar_empresas(empresas):
    print("Lista de empresas cliente: ")
    for i in range(0, empresas.longitud):
        print(f"{empresas.obtener[i].nombre}, {empresas.obtener[i].descripcion}, {empresas.obtener[i].f_creacion}, {empresas.obtener[i].direccion}, {empresas.obtener[i].correo}, {empresas.obtener[i].telefono}, {empresas.obtener[i].gerente}, {empresas.obtener[i].contacto}")
        