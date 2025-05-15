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

class GraphOnAdjacencyMatrix:
    """
    Класс для представления графа с использованием матрицы смежности.
    """
    def __init__(self, directed=False):
        """
        Инициализация графа.

        Args:
            directed (bool):  True, если граф направленный, False - если ненаправленный. По умолчанию ненаправленный.
        """
        self._vertices = []  # Список вершин графа (метки вершин).
        self._matrix = []  # Матрица смежности (двумерный список).  matrix[i][j] == 1 означает, что между вершинами i и j есть ребро.
        self._directed = directed  # Флаг, указывающий на направленность графа.

    def add_vertex(self, label):
        """
        Добавление вершины в граф.

        Args:
            label (любой тип):  Метка (идентификатор) добавляемой вершины.
        """
        if label in self._vertices:
            print(f"Вершина '{label}' уже существует.")
            return
        self._vertices.append(label)  # Добавляем метку вершины в список вершин.
        for row in self._matrix:
            row.append(0)  #  Для каждой существующей строки (вершины) добавляем столбец (в виде 0, т.к. ребра пока нет).
        self._matrix.append([0] * len(self._vertices))  # Добавляем новую строку (вершину) в матрицу смежности, заполненную нулями.

    def add_edge(self, u, v):
        """
        Добавление ребра между вершинами u и v.

        Args:
            u (любой тип): Метка первой вершины.
            v (любой тип): Метка второй вершины.
        """
        try:
            i = self._vertices.index(u)  # Находим индекс вершины u.
            j = self._vertices.index(v)  # Находим индекс вершины v.
        except ValueError:
            print("Одна из вершин не найдена.")
            return
        self._matrix[i][j] = 1  # Устанавливаем значение 1 в матрице смежности, указывая на наличие ребра из u в v.
        if not self._directed:
            self._matrix[j][i] = 1  # Если граф ненаправленный, добавляем ребро и в обратном направлении (v -> u).

    def remove_edge(self, u, v):
        """
        Удаление ребра между вершинами u и v.

        Args:
            u (любой тип): Метка первой вершины.
            v (любой тип): Метка второй вершины.
        """
        try:
            i = self._vertices.index(u)  # Находим индекс вершины u.
            j = self._vertices.index(v)  # Находим индекс вершины v.
        except ValueError:
            print("Одна из вершин не найдена.")
            return
        self._matrix[i][j] = 0  # Устанавливаем значение 0 в матрице смежности, удаляя ребро из u в v.
        if not self._directed:
            self._matrix[j][i] = 0  # Если граф ненаправленный, удаляем ребро и в обратном направлении (v -> u).

    def find_edge(self, u, v):
        """
        Проверка наличия ребра между вершинами u и v.

        Args:
            u (любой тип): Метка первой вершины.
            v (любой тип): Метка второй вершины.

        Returns:
            bool: True, если ребро существует, False - иначе.
        """
        try:
            i = self._vertices.index(u)  # Находим индекс вершины u.
            j = self._vertices.index(v)  # Находим индекс вершины v.
            return self._matrix[i][j] == 1  # Возвращаем True, если в матрице смежности значение равно 1 (ребро есть).
        except ValueError:
            return False  # Если одной из вершин нет, возвращаем False.

    def get_neighbors(self, u):
        """
        Получение списка соседей вершины u.

        Args:
            u (любой тип): Метка вершины.

        Returns:
            list: Список меток вершин, являющихся соседями вершины u.
                  Возвращает пустой список, если вершина u не найдена.
        """
        try:
            i = self._vertices.index(u)  # Находим индекс вершины u.
        except ValueError:
            print(f"Вершина '{u}' не найдена.")
            return []
        return [self._vertices[j] for j, val in enumerate(self._matrix[i]) if val == 1]  #  Возвращаем список вершин, соединенных с u.

    def __str__(self):
        """
        Возвращает строковое представление графа (матрицу смежности).

        Returns:
            str: Строка, представляющая граф.
        """
        lines = ["   " + "  ".join(str(v) for v in self._vertices)]  # Первая строка - заголовки (метки вершин).
        for label, row in zip(self._vertices, self._matrix):
            lines.append(f"{label}  " + "  ".join(str(x) for x in row))  # Для каждой вершины выводим метку и строку матрицы смежности.
        return "\n".join(lines)  # Объединяем строки в единую строку, разделяя их символом новой строки.


# Неориентированный граф
g = GraphOnAdjacencyMatrix(directed=False)
for v in range(8):
    g.add_vertex(v)

edges = [
    (0, 4), (1, 4), (1, 2), (2, 5), (4, 5),
    (4, 6), (5, 7), (6, 7)
]

for u, v in edges:
    g.add_edge(u, v)

print("Неориентированный граф:\n", g)

"""
Вывод:
Неориентированный граф:
   0  1  2  3  4  5  6  7
0  0  0  0  0  1  0  0  0
1  0  0  1  0  1  0  0  0
2  0  1  0  0  0  1  0  0
3  0  0  0  0  0  0  0  0
4  1  1  0  0  0  1  1  0
5  0  0  1  0  1  0  0  1
6  0  0  0  0  1  0  0  1
7  0  0  0  0  0  1  1  0
"""

# Проверка методов
print("\nПроверка методов (неориентированный):")
print("find_edge(1, 2):", g.find_edge(1, 2))    # True
print("find_edge(1, 7):", g.find_edge(1, 7))    # False

print("get_neighbors(4):", g.get_neighbors(4))  # [0, 1, 5, 6]

g.remove_edge(1, 2)
print("После удаления ребра (1,2):")
print("find_edge(1, 2):", g.find_edge(1, 2))    # False
print("get_neighbors(1):", g.get_neighbors(1))  # [4]

"""
Вывод:
Проверка методов (неориентированный):
find_edge(1, 2): True
find_edge(1, 7): False
get_neighbors(4): [0, 1, 5, 6]
После удаления ребра (1,2):
find_edge(1, 2): False
get_neighbors(1): [4]
"""

# Ориентированный граф
g2 = GraphOnAdjacencyMatrix(directed=True)
for v in range(8):
    g2.add_vertex(v)

directed_edges = [
    (0, 4), (1, 4), (2, 1), (4, 1), (4, 5), (4, 6),
    (5, 2), (6, 7), (7, 5)
]

for u, v in directed_edges:
    g2.add_edge(u, v)

print("\nОриентированный граф:\n", g2)

"""
Ориентированный граф:
   0  1  2  3  4  5  6  7
0  0  0  0  0  1  0  0  0
1  0  0  0  0  1  0  0  0
2  0  1  0  0  0  0  0  0
3  0  0  0  0  0  0  0  0
4  0  1  0  0  0  1  1  0
5  0  0  1  0  0  0  0  0
6  0  0  0  0  0  0  0  1
7  0  0  0  0  0  1  0  0
"""

# Проверка методов
print("\nПроверка методов (ориентированный):")
print("find_edge(2, 1):", g2.find_edge(2, 1))    # True
print("find_edge(1, 2):", g2.find_edge(1, 2))    # False

print("get_neighbors(4):", g2.get_neighbors(4))  # [1, 5, 6]

g2.remove_edge(4, 5)
print("После удаления ребра (4,5):")
print("find_edge(4, 5):", g2.find_edge(4, 5))    # False
print("get_neighbors(4):", g2.get_neighbors(4))  # [1, 6]

"""
Вывод:
Проверка методов (ориентированный):
find_edge(2, 1): True
find_edge(1, 2): False
get_neighbors(4): [1, 5, 6]
После удаления ребра (4,5):
find_edge(4, 5): False
get_neighbors(4): [1, 6]
"""