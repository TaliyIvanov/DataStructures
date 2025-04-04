"""
Здесь будет реализован алгоритм минимальной кучи

**Heap (куча)** — это специализированная структура данных на основе двоичного дерева, удовлетворяющая следующим условиям:

1. Это **полное бинарное дерево** (все уровни, кроме последнего(может быть заполнен не полностью), полностью заполнены,
а узлы последнего уровня располагаются слева направо без пропусков).
2. Выполняется **свойство кучи**:
    - В **MinHeap** значение в родительском узле меньше или равно значениям в дочерних узлах.
    - В **MaxHeap** значение в родительском узле больше или равно значениям в дочерних узлах.
3. Куча может быть помещена в массив.


"""

# Класс, реализующий структуру данных "минимальная куча" (Min Heap).
class MinHeap():
    # Инициализатор класса.
    def __init__(self):
        # Инициализирует пустой список для хранения элементов кучи.
        # Куча будет представлена в виде списка, где элементы упорядочены
        # согласно свойствам бинарной кучи.
        self.heap = []

    # Возвращает индекс родительского узла для узла с заданным индексом.
    def parent(self, index):
        # Формула для вычисления индекса родителя в бинарной куче,
        # представленной списком. Используется целочисленное деление.
        # Корень (индекс 0) не имеет родителя по этой формуле (вернет -1 или 0).
        return (index - 1) // 2

    # Возвращает индекс левого дочернего узла для узла с заданным индексом.
    def left_child(self, index):
        # Формула для вычисления индекса левого ребенка.
        return index * 2 + 1

    # Возвращает индекс правого дочернего узла для узла с заданным индексом.
    def right_child(self, index):
        # Формула для вычисления индекса правого ребенка.
        return index * 2 + 2

    # Возвращает минимальный элемент кучи (корень), не удаляя его.
    def get_min(self):
        # Проверка, не пуста ли куча.
        if self.is_empty():
            # Если куча пуста, выбрасывает исключение ValueError.
            raise ValueError('Массив пустой')
        # Минимальный элемент всегда находится в корне кучи (индекс 0).
        return self.heap[0]

    # ВНИМАНИЕ: Возвращает ПОСЛЕДНИЙ элемент в списочном представлении кучи.
    # Этот элемент НЕ обязательно является максимальным элементом во всей куче.
    # Стандартная минимальная куча не обеспечивает быстрый доступ к максимальному элементу.
    # Для нахождения максимума потребовался бы полный перебор (O(n)).
    def get_max(self):
        # Проверка на пустоту, чтобы избежать IndexError
        if self.is_empty():
             raise ValueError('Массив пустой')
        return self.heap[-1]

    # Восстанавливает свойство минимальной кучи, перемещая элемент вверх по дереву ("всплытие").
    # Элемент с индексом 'index' "всплывает" вверх по куче до тех пор,
    # пока он не станет больше или равен своему родителю, или не достигнет корня.
    def sift_up(self, index):
        # Получаем индекс родителя.
        parent_idx = self.parent(index)
        # Цикл продолжается, пока элемент не в корне (index > 0)
        # и он меньше своего родителя (нарушает свойство мин-кучи).
        while index > 0 and self.heap[parent_idx] > self.heap[index]:
            # Меняем местами текущий элемент и его родителя.
            self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
            # Переходим на уровень выше (к индексу родителя).
            index = parent_idx
            # Вычисляем индекс нового родителя.
            parent_idx = self.parent(index)

    # Восстанавливает свойство минимальной кучи, перемещая элемент вниз по дереву ("просеивание").
    # Элемент с индексом 'index' "просеивается" вниз по куче.
    # Он меняется местами с наименьшим из своих дочерних элементов,
    # если этот дочерний элемент меньше текущего. Процесс повторяется,
    # пока элемент не станет меньше или равен своим детям, или не достигнет листа.
    def sift_down(self, index):
        # Размер кучи для проверки границ.
        N = len(self.heap)
        # Цикл продолжается, пока у узла есть хотя бы один ребенок (левый).
        while self.left_child(index) < N:
            # Индекс левого ребенка.
            left = self.left_child(index)
            # Индекс правого ребенка.
            right = self.right_child(index)

            # Индекс наименьшего элемента среди текущего узла и его детей.
            # Изначально предполагаем, что текущий узел наименьший.
            min_child_idx = index

            # Если левый ребенок существует и он меньше текущего наименьшего.
            if self.heap[left] < self.heap[min_child_idx]:
                min_child_idx = left

            # Если правый ребенок существует (right < N) и он меньше текущего наименьшего
            # (который может быть уже левым ребенком).
            if right < N and self.heap[right] < self.heap[min_child_idx]:
                min_child_idx = right

            # Если текущий узел уже наименьший (меньше или равен своим детям),
            # то свойство кучи выполняется локально, и просеивание завершено.
            if min_child_idx == index:
                break # достигли нужной позиции

            # Меняем местами текущий элемент и его наименьшего ребенка.
            self.heap[index], self.heap[min_child_idx] = self.heap[min_child_idx], self.heap[index]
            # Переходим на уровень ниже (к индексу наименьшего ребенка) для продолжения просеивания.
            index = min_child_idx

    # Удаляет и возвращает минимальный элемент кучи (корень).
    def pop_min(self):
        # Если куча пуста, вернуть None (или можно выбросить исключение).
        if not self.heap:
            # raise ValueError('Куча пуста') # Альтернатива - выбросить исключение
            return None
        # Сохраняем значение минимального элемента (корень).
        min_elem = self.heap[0]
        # Если в куче больше одного элемента, перемещаем последний элемент в корень.
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop(-1) # pop(-1) удаляет и возвращает последний элемент
            # Восстанавливаем свойство кучи, просеивая новый корень вниз.
            self.sift_down(0)
        else:
            # Если в куче был только один элемент, просто очищаем ее.
            self.heap.pop(0)

        # Возвращаем сохраненный минимальный элемент.
        return min_elem

    # Добавляет новый элемент в кучу.
    def push(self, value):
        # Добавляем элемент в конец списка (на позицию нового листа).
        self.heap.append(value)
        # Восстанавливаем свойство кучи, поднимая новый элемент вверх ("всплытие").
        self.sift_up(len(self.heap) - 1)

    # Преобразует переданный список 'arr' в минимальную кучу ("пирамидизация").
    # Это более эффективный способ построить кучу из набора элементов (O(n)),
    # чем последовательное добавление (O(n log n)).
    def heapify(self, arr):
        # Используем переданный список как основу для кучи.
        self.heap = list(arr) # Создаем копию, чтобы не изменять оригинальный список arr
        # Начинаем с последнего узла, у которого есть дети (индекс N//2 - 1), и идем к корню.
        # Для каждого такого узла вызываем sift_down. Листовые элементы (с индекса N//2 до N-1)
        # уже являются кучами из одного элемента.
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            # Применяем просеивание вниз к узлу i, чтобы удовлетворить свойству кучи
            # для поддерева с корнем i.
            self.sift_down(i)

    # Проверяет, пуста ли куча.
    def is_empty(self):
        # Куча пуста, если ее внутренний список не содержит элементов.
        return len(self.heap) == 0

    # Возвращает строковое представление кучи (в виде списка).
    # Полезно для отладки и визуализации внутреннего состояния.
    def __str__(self):
        # Просто преобразуем внутренний список в строку.
        return str(self.heap)


import unittest


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap()

    def test_push_and_get_min(self):
        self.heap.push(5)
        self.heap.push(3)
        self.heap.push(8)
        self.heap.push(1)
        self.assertEqual(self.heap.get_min(), 1)

    def test_pop_min(self):
        self.heap.push(5)
        self.heap.push(3)
        self.heap.push(8)
        self.heap.push(1)
        self.assertEqual(self.heap.pop_min(), 1)
        self.assertEqual(self.heap.pop_min(), 3)
        self.assertEqual(self.heap.pop_min(), 5)
        self.assertEqual(self.heap.pop_min(), 8)
        self.assertIsNone(self.heap.pop_min())  # Проверяем на пустую кучу

    def test_heapify(self):
        arr = [5, 3, 8, 1, 2]
        self.heap.heapify(arr)
        self.assertEqual(self.heap.get_min(), 1)
        self.assertEqual(self.heap.pop_min(), 1)
        self.assertEqual(self.heap.pop_min(), 2)
        self.assertEqual(self.heap.pop_min(), 3)
        self.assertEqual(self.heap.pop_min(), 5)
        self.assertEqual(self.heap.pop_min(), 8)

    def test_is_empty(self):
        self.assertTrue(self.heap.is_empty())
        self.heap.push(10)
        self.assertFalse(self.heap.is_empty())
        self.heap.pop_min()
        self.assertTrue(self.heap.is_empty())

    def test_get_max(self):
        self.heap.push(4)
        self.heap.push(10)
        self.heap.push(2)
        self.heap.push(7)
        self.assertEqual(self.heap.get_max(), 10)
        self.heap.pop_min()
        self.assertEqual(self.heap.get_max(), 10)
        self.heap.pop_min()
        self.assertEqual(self.heap.get_max(), 10)
        self.heap.pop_min()
        self.assertEqual(self.heap.get_max(), 10)


if __name__ == "__main__":
    unittest.main()