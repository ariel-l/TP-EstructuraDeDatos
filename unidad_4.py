class EventoMedico:
    def __init__(self, tipo, descripcion, fecha):
        self.tipo = tipo
        self.descripcion = descripcion
        self.fecha = fecha
        self.hijos = []
    
    def __repr__(self):
        return f"{self.tipo} ({self.fecha}): {self.descripcion}"
    
class HistorialClinico:
    def __init__(self):
        self.raiz = None
    
    def agregar_evento (self, tipo, descripcion, fecha, padre=None):
        nuevo_evento = EventoMedico(tipo, descripcion, fecha)
        if self.raiz is None:
            self.raiz = nuevo_evento
            print(f"Evento raiz añadido: {nuevo_evento}")
        elif padre:
            padre.hijos.append(nuevo_evento)
            print(f"Evento añadido {padre}: {nuevo_evento}")
        else: print("Error encontrado: debes especificar un nodo padre")
    
    def mostrar_historial (self):
        #Muestra el historial clinico de forma jerárquica
        def mostrar_recursivo (nodo, nivel):
            if nodo is not None:
                print(" " * nivel + f"- {nodo}")
                for hijo in nodo.hijos:
                    mostrar_recursivo(hijo, nivel + 1)
        if self.raiz:
            print("Historial Clínico")
            mostrar_recursivo(self.raiz, 0)
        else: print("El historial esta vacío")
    
    def buscar_evento(self, descripcion):
        def buscar_recursivo(nodo):
            if nodo is None:
                return False
            if nodo.descripcion == descripcion:
                return nodo
            for hijo in nodo.hijos:
                resultado = buscar_recursivo(hijo)
                if resultado:
                    return resultado
            return False
        return buscar_recursivo(self.raiz)

historial = HistorialClinico()

# Agregar eventos
historial.agregar_evento("Consulta", "Consulta inicial por dolor de cabeza", "2024-11-20")
consulta = historial.raiz  # Nodo raíz
historial.agregar_evento("Diagnóstico", "Migraña crónica", "2024-11-21", consulta)
diagnostico = consulta.hijos[0]
historial.agregar_evento("Tratamiento", "Receta de analgésicos", "2024-11-22", diagnostico)
historial.agregar_evento("Seguimiento", "Control después de un mes", "2024-12-22", consulta)

# Mostrar el historial clínico
historial.mostrar_historial()

# Buscar un evento específico
print("\nBuscar evento con descripción 'Receta de analgésicos':")
evento = historial.buscar_evento("Receta de analgésicos")
print(evento if evento else "Evento no encontrado")