import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Lista de usuarios
usuarios = ["Antonio", "Carmen", "Manuel", "Lola", "Rocío"]

# Conexiones entre usuarios con etiquetas para las aristas
conexiones = [
    ("Antonio", "Carmen", {"relacion": "sigue"}),  # Antonio sigue a Carmen
    ("Carmen", "Manuel", {"relacion": "mejores amigos"}),  # Carmen y Manuel son mejores amigos
    ("Manuel", "Lola", {"relacion": "sigue"}),  # Manuel sigue a Lola
    ("Lola", "Antonio", {"relacion": "sigue"}),  # Lola sigue a Antonio (ciclo)
    ("Antonio", "Rocío", {"relacion": "sigue"}),  # Antonio sigue a Rocío
    ("Rocío", "Carmen", {"relacion": "sigue"}),  # Rocío sigue a Carmen
]

# Añadir nodos y aristas al grafo
G.add_nodes_from(usuarios)
G.add_edges_from((u, v, data) for u, v, data in conexiones)

# Generar la disposición de los nodos
pos = nx.spring_layout(G)

# Dibujar nodos y aristas
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, edge_color="gray")

# Añadir etiquetas a las aristas
# Crear un diccionario vacío para las etiquetas de las aristas
edge_labels = {}

# Recorrer cada arista del grafo y extraer la información
for u, v, data in G.edges(data=True):
    # Obtener la relación desde los datos de la arista
    etiqueta = data["relacion"]
    # Añadir la etiqueta al diccionario con la clave (u, v)
    edge_labels[(u, v)] = etiqueta

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Mostrar el grafo
plt.title("Grafo de Segudores de Insta")
plt.show()
