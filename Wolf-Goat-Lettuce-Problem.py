# Iniciamos creando el grafo dado y el nodo inicial
import matplotlib.pyplot as plt
import networkx as nx


grafo = {
    'wglf|': ['glw|f', 'lw|fg', 'gw|fl', 'gl|fw'],
    'gl|fw': [],
    'glw|f': [],
    'gw|fl': [],
    'lw|fg': ['wglf|', 'flw|g'],
    'flw|g': ['lw|fg', 'l|fgw', 'w|fgl'],
    'l|fgw': ['fl|gw','fgl|w','flw|g'],
    'fl|gw': [],
    'fgl|w': ['l|fgw','g|flw','gl|fw'],
    'w|fgl': ['flw|g','fw|gl','fgw|l'],
    'fw|gl': [],
    'fgw|l': ['gw|fl', 'w|fgl', 'g|flw'],
    'g|flw': ['fgl|w', 'fgw|l', 'fg|lw'],
    'fg|lw': ['g|flw','|fglw'],
    '|fglw': []
}

inicio = 'wglf|'
final = '|fglw'

# Función DFS para un grafo de enteros
def dfs(grafo, inicio, final):
    # Inicializar pila y visitados
    pila = [(inicio, [inicio])]
    visitados = set()

    # Crear grafo con adyacentes del camino más corto
    def crear_grafo_corto(camino_corto):
        grafo_corto = {}
        for i in range(len(camino_corto)):
            nodo = camino_corto[i]
            if i < len(camino_corto) - 1:
                siguiente = camino_corto[i+1]
                adyacentes = [siguiente]
                if nodo in grafo_corto:
                    adyacentes += [a for a in grafo_corto[nodo] if a == siguiente]
                grafo_corto[nodo] = adyacentes
            else:
                grafo_corto[nodo] = []
        return grafo_corto

    # Recorrer pila hasta que esté vacía
    while pila:
        (nodo_actual, camino) = pila.pop()

        # Si encontramos el nodo final, regresar el camino y el grafo corto
        if nodo_actual == final:
            grafo_corto = crear_grafo_corto(camino)
            return (camino, grafo_corto)

        # Si no ha sido visitado el nodo actual, marcarlo como visitado y agregar adyacentes a la pila
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            for adyacente in grafo[nodo_actual]:
                if adyacente not in visitados:
                    pila.append((adyacente, camino + [adyacente]))

    # Si no se encuentra camino, regresar None
    return None

(camino_corto, grafo_corto) = dfs(grafo, inicio, final)




# Función para calcular las distancias del nodo inicial a los demás nodos del grafo
def calcular_distancias(grafo, inicio):
    # Inicializar la distancia del nodo inicial como 0
    distancias = {inicio: 0}
    cola = [inicio]  # Inicializar la cola con el nodo inicial
    while cola:
        nodo = cola.pop(0)
        for adyacente in grafo.get(nodo, []):
            if adyacente not in distancias:
                distancias[adyacente] = distancias[nodo] + 1
                cola.append(adyacente)
    return distancias


# Función para graficar el grafo del camino mas corto
def graficar_nodos(grafo, camino_corto, distancias):
    # Titulo al grafico de los NODOS
    plt.title("Problema del barquito, solucionado mediante DFS")
    G = nx.DiGraph()  # Crear un grafo dirigido y lo almacena en la variable G
    # Agregar nodos al grafo
    for nodo in camino_corto:  # Agregamos los Nodos del camino corto a la variable G
        G.add_node(nodo)
    # Agregar aristas al grafo
    # Agrega las aristas del camino corto mediante el diccionario de distancias (adyacentes)
    for i in range(len(camino_corto)-1):
        nodo = camino_corto[i]
        adyacente = camino_corto[i+1]
        G.add_edge(nodo, adyacente)
    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_size=1200, with_labels=True )
      # Agregar etiquetas de distancia
    for nodo in G.nodes:
        if nodo in distancias:
            distancia = distancias[nodo]
            pos_nodo = pos[nodo]
            label_pos = (pos_nodo[0], pos_nodo[1] + 0.1)
            plt.text(*label_pos, str(distancia), horizontalalignment='center', fontsize=14)

    plt.show()  # Muestra el grafico





# Impresion de DFS, Distancia y grafico con la libreria Matplotlib
print("\nRecorrido DFS:\n ".join(camino_corto))
print("\nDistancia del nodo inicial:")
distancias = calcular_distancias(grafo, inicio)
for nodo, distancia in distancias.items():
    print("Nodo: {} - Distancia: {}".format(nodo, distancia))
print("\nGrafica del grafo:")
graficar_nodos(grafo, camino_corto, distancias)