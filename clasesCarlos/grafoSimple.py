# Representación de un grafo no dirigido
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Imprimir nodos y aristas
for nodo, adyacentes in grafo.items():
    print(f"Nodo {nodo}: conectado con {adyacentes}")

