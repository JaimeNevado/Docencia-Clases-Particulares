import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

G.add_nodes_from(["A", "B", "C", "D", "E", "F"])
# Añadir nodos y aristas
G.add_edges_from([
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "E"),
    ("E", "F"),
])

# Búsqueda en profundidad desde el nodo "A"
dfs_result = list(nx.dfs_edges(G, source="A"))
print("Búsqueda en profundidad (aristas):", dfs_result)

# Búsqueda en profundidad (orden de los nodos)
dfs_nodes = list(nx.dfs_preorder_nodes(G, source="A"))
print("Búsqueda en profundidad (nodos):", dfs_nodes)


# Configuración de la visualización
pos = nx.spring_layout(G)

# Dibujar nodos y aristas
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightgreen", font_size=10, edge_color="gray")

# Mostrar el grafo
plt.title("Grafo con Búsqueda en Anchura")
plt.show()