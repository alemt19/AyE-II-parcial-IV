class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.fin = None
    def esta_vacia(self):
        return self.frente is None
    
    def agregar(self, valor):
        nodo_nuevo = Nodo(valor)
        if self.esta_vacia():
            self.frente = nodo_nuevo
        else:
            self.fin.siguiente = nodo_nuevo
        self.fin = nodo_nuevo
    def eliminar_frente(self,valor):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.frente.valor
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.fin = None
            return valor_eliminado
    def eliminar(self, valor):
        if self.esta_vacia():
            return None
        
        # Si el valor a eliminar está en el frente de la cola
        if self.frente.valor == valor:
            return self.eliminar_frente()

        # Si el valor a eliminar está en el medio o al final de la cola
        nodo_actual = self.frente
        while nodo_actual.siguiente is not None:
            if nodo_actual.siguiente.valor.nombre == valor:
                nodo_a_eliminar = nodo_actual.siguiente
                nodo_actual.siguiente = nodo_a_eliminar.siguiente
                if nodo_a_eliminar == self.fin:
                    self.fin = nodo_actual
                return nodo_a_eliminar.valor.nombre
            nodo_actual = nodo_actual.siguiente
        
        return None  # Si el valor no se encuentra en la cola

    def ver_frente(self):
        if self.esta_vacia():
            return None
        else:
            return self.frente.valor
        
    def recorrer(self):
        if self.esta_vacia():
            print("La cola está vacía")
        else:
            self._recorrer_aux(self.frente)
    def _recorrer_aux(self, nodo):
        if nodo is not None:
            print("proyectos actuales:")
            print(f"-{nodo.valor.nombre}")
            self._recorrer_aux(nodo.siguiente)
    def buscar_nombre(self, nombre):
        actual = self.frente
        while actual:
            if actual.valor.nombre == nombre:
                return True
            actual = actual.siguiente
        return False
    def devolver_objeto(self, nombre):
        actual = self.frente
        while actual:
            if actual.valor.nombre == nombre:
                return actual.valor
            actual = actual.siguiente
        return False
    
        



