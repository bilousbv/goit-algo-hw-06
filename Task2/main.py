import os
import importlib.util
from collections import deque

# Вкажіть абсолютний шлях до файлу Task1/main.py
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Task1/main.py'))
spec = importlib.util.spec_from_file_location("main", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Створюємо граф, викликаючи функцію create_graph
G = module.create_graph()

# Алгоритм DFS
def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for neighbor in set(graph.neighbors(vertex)) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            else:
                stack.append((neighbor, path + [neighbor]))

# Алгоритм BFS
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for neighbor in set(graph.neighbors(vertex)) - set(path):
            if neighbor == goal:
                return path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))

# Визначення початкової та кінцевої станції
start_station = "Station A"
end_station = "Station G"

# Знаходження шляхів з використанням DFS і BFS
path_dfs = dfs(G, start_station, end_station)
path_bfs = bfs(G, start_station, end_station)

# Виведення результатів
print("Шлях DFS:", path_dfs)
print("Шлях BFS:", path_bfs)