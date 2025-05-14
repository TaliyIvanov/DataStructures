"""
Here i will realize class Graph on EdgeList

Complexity:
Memory - O(V+E)
AddVertex - O(1)
AddEdge - O(1)
RemoveEdge - O(E)
FindEdge - O(1)
GetNeighbors - O(E)
"""

class GraphOnAdjacencyList:
    """
    Класс, представляющий граф, реализованный на основе списка смежности.
    Attributes:
        adjacency_list (dict): Словарь, где ключами являются вершины графа,
                               а значениями - списки смежных вершин (соседей).
        directed (bool): Флаг, указывающий, является ли граф направленным (True)
                         или ненаправленным (False). По умолчанию - ненаправленный.
    """
    def __init__(self, directed=False):
        """
        Конструктор класса.
        Args:
            directed (bool, optional):  Указывает, является ли граф направленным.
                                         По умолчанию (False) создается ненаправленный граф.
        """
        self.adjacency_list = {}  # Словарь, представляющий список смежности. Ключи - вершины, значения - списки смежных вершин.
        self.directed = directed  # Флаг, указывающий на направленность графа.

    def add_vertex(self, v):
        """
        Добавляет вершину в граф.
        Args:
            v: Вершина, которую нужно добавить.
        """
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []  # Инициализируем пустой список смежности для новой вершины.

    def add_edge(self, v, u):
        """
        Добавляет ребро между вершинами v и u.
        Args:
            v: Начальная вершина ребра.
            u: Конечная вершина ребра.
        """
        self.add_vertex(v)  # Добавляем вершину v, если ее еще нет в графе.
        self.add_vertex(u)  # Добавляем вершину u, если ее еще нет в графе.
        if u not in self.adjacency_list[v]:
            self.adjacency_list[v].append(u)  # Добавляем u в список смежности для v.

        if not self.directed and v not in self.adjacency_list[u]:  # Если граф ненаправленный,
                                                                   # добавляем ребро и в обратном направлении.
            self.adjacency_list[u].append(v)

    def remove_edge(self, v, u):
        """
        Удаляет ребро между вершинами v и u.
        Args:
            v: Начальная вершина ребра.
            u: Конечная вершина ребра.
        """
        if v in self.adjacency_list and u in self.adjacency_list[v]:
            self.adjacency_list[v].remove(u)  # Удаляем u из списка смежности для v.

        if not self.directed and u in self.adjacency_list and v in self.adjacency_list[u]:  # Если граф ненаправленный,
                                                                                          # удаляем ребро и в обратном направлении.
            self.adjacency_list[u].remove(v)

    def find_edge(self, v, u):
        """
        Проверяет, существует ли ребро между вершинами v и u.
        Args:
            v: Начальная вершина ребра.
            u: Конечная вершина ребра.

        Returns:
            bool: True, если ребро существует, False в противном случае.
        """
        return v in self.adjacency_list and u in self.adjacency_list[v]  # Проверяем, что v есть в графе и u есть в списке смежности для v.

    def get_neighbors(self, v):
        """
        Возвращает список соседей вершины v.
        Args:
            v: Вершина, для которой нужно получить соседей.

        Returns:
            list: Список соседей вершины v. Возвращает пустой список, если вершина не найдена.
        """
        return self.adjacency_list.get(v, [])  # Возвращает список соседей вершины v или пустой список, если вершины нет.

    def __str__(self):
        """
        Возвращает строковое представление графа.
        Returns:
            str: Строка, представляющая граф в формате: "вершина: [соседи]".
        """
        return "\n".join(f"{v}: {sorted(neighbors)}" for v, neighbors in sorted(self.adjacency_list.items()))  # Формирует строку, представляющую граф.  Сортировка для предсказуемого вывода.

# Создание графа
g = GraphOnAdjacencyList(directed=False)

# Добавим вершины (включая изолированную)
for v in range(8):
    g.add_vertex(v)

# Добавим рёбра
edges = [
    (0, 4),
    (1, 4), (1, 2),
    (2, 5),
    (4, 5), (4, 6),
    (5, 7),
    (6, 7)
]

for v, u in edges:
    g.add_edge(v, u)

print("Списки смежности:")
print(g)

"""
Вывод:
Списки смежности:
0: [4]
1: [2, 4]
2: [1, 5]
3: []
4: [0, 1, 5, 6]
5: [2, 4, 7]
6: [4, 7]
7: [5, 6]

Process finished with exit code 0
"""

