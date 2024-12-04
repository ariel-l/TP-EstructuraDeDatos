from collections import deque

grafo = {
    "Hospital A": ["Hospital B", "Hospital C"],
    "Hospital B": ["Hospital D", "Hospital E"],
    "Hospital C": ["Hospital E"],
    "Hospital D": ["Hospital F"],
    "Hospital E": ["Hospital F"],
    "Hospital F": []
}

def bfs_camino_mas_corto(grafo, inicio, objetivo):

    cola = deque([(inicio, [inicio])])

    def procesar(cola):
        if not cola:
            return None

        nodo_actual, camino = cola.popleft()
        if nodo_actual == objetivo:
            return camino

        for vecino in grafo[nodo_actual]:
            if vecino not in camino:
                cola.append((vecino, camino + [vecino]))

        return procesar(cola)

    return procesar(cola)

def dfs_encontrar_camino(grafo, inicio, objetivo, visitados=None, camino=None):

    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []

    visitados.add(inicio)
    camino.append(inicio)

    if inicio == objetivo:
        return camino

    for vecino in grafo[inicio]:
        if vecino not in visitados:
            resultado = dfs_encontrar_camino(grafo, vecino, objetivo, visitados, camino)
            if resultado:
                return resultado

    camino.pop()
    return None

"""
# Invocaciones
hospital_origen = "Hospital A"
hospital_destino = "Hospital F"

camino_bfs = bfs_camino_mas_corto(grafo, hospital_origen, hospital_destino)
camino_dfs = dfs_encontrar_camino(grafo, hospital_origen, hospital_destino)

print("Camino más corto con BFS:", camino_bfs)
print("Camino encontrado con DFS:", camino_dfs)
"""