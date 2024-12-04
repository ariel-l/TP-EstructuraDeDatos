import heapq

def dijkstra(grafo, inicio):
    distancias = {hospital: float('inf') for hospital in grafo}
    distancias[inicio] = 0 
    
    cola_prioridad = [(0, inicio)]  # (distancia, nodo)
    
    while cola_prioridad:
        distancia_actual, hospital_actual = heapq.heappop(cola_prioridad)
        
        if distancia_actual > distancias[hospital_actual]:
            continue
        
        for vecino in grafo[hospital_actual]:
            distancia = distancia_actual + 1  # Asumimos que todos los caminos tienen peso 1
            
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))
    
    return distancias

grafo = {
    "Hospital A": ["Hospital B", "Hospital C"],
    "Hospital B": ["Hospital D", "Hospital E"],
    "Hospital C": ["Hospital E"],
    "Hospital D": ["Hospital F"],
    "Hospital E": ["Hospital F"],
    "Hospital F": []
}
"""
hospital_inicio = "Hospital A"
caminos_minimos = dijkstra(grafo, hospital_inicio)

print(f"Distancias mínimas desde {hospital_inicio}: {caminos_minimos}")
"""