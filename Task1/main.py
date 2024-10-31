# graph_data.py
import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    graph = nx.Graph()

    # Додаємо вузли
    stations = [
        "Station A", "Station B", "Station C", "Station D", "Station E",
        "Station F", "Station G", "Station H", "Station I", "Station J"
    ]
    graph.add_nodes_from(stations)

    # Додаємо ребра
    connections = [
        ("Station A", "Station B", 5),
        ("Station A", "Station C", 3),
        ("Station B", "Station D", 2),
        ("Station C", "Station D", 7),
        ("Station D", "Station E", 3),
        ("Station E", "Station F", 1),
        ("Station F", "Station G", 6),
        ("Station G", "Station H", 4),
        ("Station H", "Station I", 2),
        ("Station I", "Station J", 8),
        ("Station J", "Station A", 10)
    ]

    for station1, station2, weight in connections:
        graph.add_edge(station1, station2, weight=weight)

    # graph.add_edges_from(connections)

    return graph


if __name__ == "__main__":
    G = create_graph()

    # Візуалізація графа
    plt.figure(figsize=(10, 8))
    nx.draw(G, with_labels=True, node_color="lightblue", font_weight="bold", node_size=1000, edge_color="gray")
    plt.title("Транспортна мережа міста (мережа метро)")
    plt.show()

    # Аналіз характеристик графа
    # Кількість вершин
    num_nodes = G.number_of_nodes()
    print("Кількість станцій (вершин):", num_nodes)

    # Кількість ребер
    num_edges = G.number_of_edges()
    print("Кількість сполучень (ребер):", num_edges)

    # Ступінь кожної вершини
    degree = dict(G.degree())
    print("Ступінь кожної станції:")
    for station, deg in degree.items():
        print(f"{station}: {deg}")

