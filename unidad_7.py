import networkx as nx
import matplotlib.pyplot as plt

# Creamos el grafo
red_hospitales = nx.Graph()

# Añadir nodos (hospitales)
red_hospitales.add_node("Hospital A")
red_hospitales.add_node("Hospital B")
red_hospitales.add_node("Clínica C")
red_hospitales.add_node("Clínica D")

# Añadir aristas con distancias
red_hospitales.add_edge("Hospital A", "Hospital B", weight=10)  
red_hospitales.add_edge("Hospital A", "Clínica C", weight=15)  
red_hospitales.add_edge("Hospital B", "Clínica D", weight=5)   
red_hospitales.add_edge("Clínica C", "Clínica D", weight=20) 

# Dibujar el grafo
pos = nx.spring_layout(red_hospitales)  # Layout para posicionar los nodos


nx.draw(red_hospitales, pos, with_labels=True, node_size=2000, node_color="lightblue")

distances = nx.get_edge_attributes(red_hospitales, 'weight')
nx.draw_networkx_edge_labels(red_hospitales, pos, edge_labels=distances)

# Mostrar el grafo
plt.title("Red de Hospitales y Clínicas")
plt.show()


