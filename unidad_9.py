from collections import defaultdict, deque

class Diagnostico:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_nodo(self, nodo):
        if not nodo:
            raise ValueError("El nodo no puede ser nulo o vacío.")
        self.grafo[nodo]

    def agregar_dependencia(self, paso_previo, paso_siguiente):
        if not paso_previo or not paso_siguiente:
            raise ValueError("Los pasos no pueden ser nulos o vacíos.")
        self.agregar_nodo(paso_previo)
        self.agregar_nodo(paso_siguiente)
        self.grafo[paso_previo].append(paso_siguiente)

    def orden_topologico(self):
        grados_entrada = defaultdict(int)
        for nodo in self.grafo:
            for vecino in self.grafo[nodo]:
                grados_entrada[vecino] += 1

        cola = deque([nodo for nodo in self.grafo if grados_entrada[nodo] == 0])

        orden = []
        while cola:
            actual = cola.popleft()
            orden.append(actual)

            for vecino in self.grafo[actual]:
                grados_entrada[vecino] -= 1
                if grados_entrada[vecino] == 0:
                    cola.append(vecino)

        if len(orden) != len(self.grafo):
            nodos_con_ciclo = [nodo for nodo, grado in grados_entrada.items() if grado > 0]
            raise ValueError(f"El grafo contiene ciclos. Nodos involucrados: {', '.join(nodos_con_ciclo)}")

        return orden

    def detectar_nodos_aislados(self):
        grados_entrada = defaultdict(int)
        for nodo in self.grafo:
            for vecino in self.grafo[nodo]:
                grados_entrada[vecino] += 1

        aislados = [nodo for nodo in self.grafo if not self.grafo[nodo] and grados_entrada[nodo] == 0]
        return aislados

if __name__ == "__main__":
    diagnostico = Diagnostico()
    diagnostico.agregar_dependencia("Revisar antecedentes médicos", "Registrar síntomas")
    diagnostico.agregar_dependencia("Registrar síntomas", "Decidir pruebas")
    diagnostico.agregar_dependencia("Decidir pruebas", "Pruebas básicas")
    diagnostico.agregar_dependencia("Pruebas básicas", "Evaluar resultados básicos")
    diagnostico.agregar_dependencia("Evaluar resultados básicos", "Pruebas avanzadas")
    diagnostico.agregar_dependencia("Pruebas avanzadas", "Confirmar diagnóstico")

    try:
        orden = diagnostico.orden_topologico()
        print("Orden de pasos para el diagnóstico:")
        print(" -> ".join(orden))

        nodos_aislados = diagnostico.detectar_nodos_aislados()
        if nodos_aislados:
            print(f"Atención: Los siguientes pasos no están conectados: {', '.join(nodos_aislados)}")
    except ValueError as e:
        print(e)
