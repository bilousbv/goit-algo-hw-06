import os
import importlib.util
import networkx as nx

# Вкажіть абсолютний шлях до файлу Task1/main.py
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Task1/main.py'))
spec = importlib.util.spec_from_file_location("main", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Створюємо граф, викликаючи функцію create_graph
G = module.create_graph()


# Функція для знаходження найкоротшого шляху від кожної вершини до всіх інших
def dijkstra_all_pairs(graph):
    shortest_paths = {}
    for node in graph.nodes:
        # Використовуємо алгоритм Дейкстри для знаходження найкоротшого шляху від `node` до всіх інших вузлів
        lengths = nx.single_source_dijkstra_path_length(graph, node)
        shortest_paths[node] = lengths
    return shortest_paths

# Знаходимо найкоротший шлях між усіма вершинами
shortest_paths = dijkstra_all_pairs(G)

# Виводимо результати
for start_node, paths in shortest_paths.items():
    print(f"Найкоротші шляхи від {start_node}:")
    for end_node, distance in paths.items():
        print(f" - До {end_node}: {distance} одиниць")