"""
Here i will realize class Graph on EdgeList

Complexity:
Memory - O(E)
AddVertex - O(1)
AddEdge - O(E)
RemoveEdge - O(E)
FindEdge - O(E)
GetNeighbors - O(E)
"""

class Graph_on_EdgeList:
    """
    Класс для представления графа с использованием списка ребер.

    Attributes:
        vertices (set): Множество уникальных вершин графа.
        edges (list): Список ребер графа.  Каждое ребро - это кортеж (u, v), где u - начальная вершина, v - конечная вершина.
        directed (bool):  True, если граф направленный, False - если ненаправленный.
    """
    def __init__(self, directed=False):
        """
        Инициализация графа.

        Args:
            directed (bool):  Флаг, указывающий, является ли граф направленным (по умолчанию False).
        """
        self.vertices = set()    # Множество уникальных вершин графа
        self.edges = []          # Список ребер (u, v)
        self.directed = directed # Флаг, указывающий на направленность графа

    def add_vertex(self, v):
        """
        Добавляет вершину в граф.

        Args:
            v: Вершина, которую нужно добавить.
        """
        self.vertices.add(v)  # Добавляем вершину в множество вершин

    def add_edge(self, u, v):
        """
        Добавляет ребро в граф.

        Args:
            u: Начальная вершина ребра.
            v: Конечная вершина ребра.
        """
        self.add_vertex(u) # Добавляем вершину u (если ее еще нет)
        self.add_vertex(v) # Добавляем вершину v (если ее еще нет)
        edge = (u, v)      # Создаем кортеж, представляющий ребро
        if edge not in self.edges: # Проверяем, существует ли ребро в списке
            self.edges.append(edge)  # Добавляем ребро в список ребер (если его там еще нет)

        # Если граф ненаправленный, добавляем обратное ребро (v, u), чтобы отразить двунаправленность.
        if not self.directed and edge not in self.edges:
            self.edges.append(edge)

    def remove_edge(self, u, v):
        """
        Удаляет ребро из графа.

        Args:
            u: Начальная вершина ребра.
            v: Конечная вершина ребра.
        """
        edge = (u,v)  # Создаем кортеж, представляющий ребро
        if edge in self.edges:  # Проверяем, существует ли ребро в списке
            self.edges.remove(edge)  # Удаляем ребро

        # Если граф ненаправленный, удаляем и обратное ребро.
        if not self.directed:
            rev_edge = (u, v) # Создаем кортеж, представляющий обратное ребро.
            if rev_edge in self.edges:  # Проверяем, существует ли обратное ребро.
                self.edges.remove(rev_edge)  # Удаляем обратное ребро.

    def find_edge(self, u, v):
        """
        Проверяет, существует ли ребро между вершинами u и v.

        Args:
            u: Начальная вершина ребра.
            v: Конечная вершина ребра.

        Returns:
            bool: True, если ребро существует, иначе False.
        """
        # Проверяем наличие ребра (u, v) или (v, u) для ненаправленного графа.
        return (u, v) in self.edges or (not self.directed and (v, u) in self.edges)

    def get_neighbors(self,v):
        """
        Возвращает список соседей для данной вершины.

        Args:
            v: Вершина, для которой нужно найти соседей.

        Returns:
            list: Список вершин, смежных с v.
        """
        neighbors = []
        for (src, dst) in self.edges:  # Перебираем все ребра
            if src == v:  # Если текущее ребро исходит из вершины v
                neighbors.append(dst)  # Добавляем вершину назначения (dst) в список соседей
        return neighbors # Возвращаем список соседей

g = Graph_on_EdgeList(directed=False)

# Добавим рёбра
edge_list = [
    (0, 4),
    (4, 1),
    (1, 2),
    (2, 5),
    (4, 5),
    (4, 6),
    (5, 7),
    (6, 7)
]

for u, v in edge_list:
    g.add_edge(u, v)

# === Демонстрация работы методов ===
print("Список всех вершин:", sorted(g.vertices))              # [0, 1, 2, 4, 5, 6, 7]
print("Список всех рёбер:", g.edges)                         # Покажет пары (в обе стороны)
print("Соседи вершины 4:", g.get_neighbors(4))               # [0, 1, 5, 6]
print("Есть ли ребро между 4 и 5?", g.find_edge(4, 5))       # True
print("Есть ли ребро между 3 и 0?", g.find_edge(3, 0))       # False

"""
Вывод:
Список всех вершин: [0, 1, 2, 4, 5, 6, 7]
Список всех рёбер: [(0, 4), (4, 1), (1, 2), (2, 5), (4, 5), (4, 6), (5, 7), (6, 7)]
Соседи вершины 4: [1, 5, 6]
Есть ли ребро между 4 и 5? True
Есть ли ребро между 3 и 0? False
"""