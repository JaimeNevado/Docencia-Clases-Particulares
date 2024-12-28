import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido (porque las reacciones tienen una dirección)
G = nx.DiGraph()

# Añadir nodos (metabolitos)
metabolitos = ["alcohol_primario", "NAD+", "aldeido", "NADH", "H+", "fructosa"]
for metabolito in metabolitos:
    G.add_node(metabolito)

# Añadir aristas (reacciones)
G.add_edge("alcohol_primario", "aldeido", enzima="1.1.1.1", numero_reaccion=1,
           reactivos=[["alcohol_primario", 1], ["NAD+", 1]],
           productos=[["aldeido", 1], ["NADH", 1], ["H+", 1]])

G.add_edge("aldeido", "fructosa", tipo="espontanea", id_reaccion=2,
           reactivos=[["aldeido", 1]],
           productos=[["fructosa", 1]])

# Configuración de la visualización
pos = nx.spring_layout(G)  # Disposición de los nodos

# Dibujar nodos y aristas
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, edge_color="gray")

# Añadir etiquetas a las aristas con la información de la reacción
edge_labels = {}
for u, v, data in G.edges(data=True):
    if "enzima" in data:
        label = f"Enzima: {data['enzima']} (Rx {data['numero_reaccion']})"
    elif "tipo" in data:
        label = f"Tipo: {data['tipo']}"
    edge_labels[(u, v)] = label

# Dibujar las etiquetas de las aristas
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Mostrar el grafo
plt.title("Grafo de Reacciones Químicas")
plt.show()
