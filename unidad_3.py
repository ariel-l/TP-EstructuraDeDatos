from unit_1 import Paciente

class NodoPaciente ():
    def __init__(self, paciente):
        self.paciente = paciente
        self.izquierdo = None
        self.derecho = None

class ArbolPacientes ():
    def __init__(self):
        self.raiz = None
    
    def insertar(self, Paciente):
        def insertar_recursivo (nodo, nuevo_paciente):
            if nuevo_paciente.ID < nodo.paciente.ID:
                if nodo.izquierdo is None:
                    nodo.izquierdo = NodoPaciente(nuevo_paciente)
                else: 
                    insertar_recursivo(nodo.izquierdo, nuevo_paciente)
            elif nuevo_paciente.ID > nodo.paciente.ID:
                if nodo.derecho is None:
                    nodo.derecho = NodoPaciente(nuevo_paciente)
                else: 
                    insertar_recursivo (nodo.derecho, nuevo_paciente)
        if self.raiz is None:
            self.raiz = NodoPaciente(Paciente)
        else: insertar_recursivo(self.raiz, Paciente)
   
    def buscar(self, ID):
        #Busca un paciente en el arbol por su ID
        def buscar_recursivo (nodo, ID):
            if nodo is None:
                return None
            if nodo.paciente.ID == ID:
                return nodo.paciente
            elif ID < nodo.paciente.ID:
                return buscar_recursivo(nodo.izquierdo, ID)
            else: 
                return buscar_recursivo(nodo.derecho, ID)
        return buscar_recursivo(self.raiz, ID)
    
    def eliminar(self, ID):
        #Elimina un paciente del arbol por su ID
        def eliminar_recursivo(nodo, ID):
            if nodo is None:
                return nodo
            if ID < nodo.paciente.ID:
                nodo.izquierdo = eliminar_recursivo(nodo.izquierdo, ID)
            elif ID > nodo.paciente.ID:
                nodo.derecho = eliminar_recursivo(nodo.derecho, ID)
            else:
                #nodo sin hijos
                if nodo.izquierdo is None and nodo.derecho is None:  
                    return None
                #nodo con 1 solo hijo
                elif nodo.izquierdo is None:                         
                    return nodo.derecho
                elif nodo.derecho is None:
                    return nodo.izquierdo
                #nodo con 2 hijos
                sucesor = self._minimo(nodo.derecho)
                nodo.paciente = sucesor.paciente
                nodo.derecho = eliminar_recursivo(nodo.derecho, sucesor.paciente.ID)
            return nodo
        self.raiz = eliminar_recursivo(self.raiz, ID)
    
    def _minimo(self, nodo):
        #Encuentra el nodo con el ID minimo en un subarbol
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo
    def en_orden(self):
        def en_orden_recursivo(nodo, resultado):
            if nodo is not None:
                en_orden_recursivo(nodo.izquierdo, resultado)
                resultado.append(nodo.paciente)
                en_orden_recursivo(nodo.derecho, resultado)
        resultado = []
        en_orden_recursivo(self.raiz, resultado)
        return resultado


# Crear el árbol
arbol = ArbolPacientes ()

# Insertar pacientes
arbol.insertar(Paciente("Juan Pérez", 30, 3, "juanperez@gmail.com", 12345678, "ioma"))
arbol.insertar(Paciente("María Gómez", 25, 1, "mariagomez@gmail.com", 11111111, "ioma"))
arbol.insertar(Paciente("Carlos Ruiz", 40, 5, "carlosruiz@gmail.com", 22222222, "osecac"))
arbol.insertar(Paciente("Ana Torres", 20, 2, "anatorres@hmail.com", 33333333, "ioma"))
arbol.insertar(Paciente("Luis Vega", 35, 4, "luisvega@gmail.com", 44444444, "osecac"))

# Mostrar los pacientes en orden ascendente por ID
print("Pacientes en orden:")
print(arbol.en_orden())

# Buscar un paciente por ID
print("\nBuscar paciente con ID 2:")
paciente = arbol.buscar(2)
print(paciente if paciente else "Paciente no encontrado")

# Eliminar un paciente por ID
print("\nEliminar paciente con ID 3:")
arbol.eliminar(3)
print("Pacientes después de la eliminación:")
print(arbol.en_orden())
