"""
Двусвязный список — это структура данных, состоящая из узлов (элементов),
каждый из которых содержит **три части**:

1. **Данные** (значение узла).
2. **Ссылку на следующий узел** (next).
3. **Ссылку на предыдущий узел** (prev).

В отличие от **односвязного списка**, в котором каждый узел содержит только ссылку
на следующий элемент, в **двусвязном списке** можно перемещаться в **обе стороны**.

| Метод                  | Описание                                     |
| ---------------------- | -------------------------------------------- |
| `append(value)`        | Добавляет элемент в конец списка             |
| `prepend(value)`       | Добавляет элемент в начало списка            |
| `insert(index, value)` | Вставляет элемент по индексу                 |
| `remove(value)`        | Удаляет первый найденный элемент по значению |
| `pop()`                | Удаляет последний элемент                    |
| `pop_first()`          | Удаляет первый элемент                       |
| `find(value)`          | Возвращает `True`, если элемент найден       |
| `reverse()`            | Разворачивает список                         |
| `display()`            | Выводит элементы списка                      |
"""


class DoubleLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None #
            self.prev = None # link to previously Node

    def __init__(self):
        self.root = None # first elem
        self.tail = None # last elem
        self.size = 0 # count elements

    # insert elem in tail in list
    def append(self, value):
        new_node = self.Node(value)
        if not self.root: # if list is empty
            self.root = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    # insert elem in head of list
    def prepend(self, value):
        new_node = self.Node(value)
        if not self.root: # if list is empty
            self.root = self.tail = new_node
        else:
            new_node.next = self.root
            self.root.prev = new_node
            self.root = new_node
        self.size += 1
    # insert elem to index
    def insert(self, i, value):
        if i < 0 or i > self.size:
            raise IndexError("Index out of bounds")

        if i == 0:
            self.prepend(value)
            return
        if i == self.size:
            self.append(value)
            return

        new_node = self.Node(value)
        runner = self.root
        for _ in range(i - 1):  # Доходим до узла перед нужным индексом
            runner = runner.next

        new_node.next = runner.next
        new_node.prev = runner
        runner.next.prev = new_node
        runner.next = new_node

        self.size += 1

    # delete first find elem
    def remove(self,value):
        current = self.root
        while current:
            if current.value == value:
                if current == self.root:  # Удаление первого элемента
                    self.root = current.next
                    if self.root:
                        self.root.prev = None
                elif current == self.tail:  # Удаление последнего элемента
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:  # Удаление элемента в середине
                    current.prev.next = current.next
                    current.next.prev = current.prev

                if self.root is None:  # Если список стал пустым
                    self.tail = None

                self.size -= 1
                return
            current = current.next

    # return and delete last elem
    def pop(self):
        if self.tail is None:
            return None
        result = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.root = None  # Список стал пустым
        self.size -= 1
        return result
    # return and delete first elem
    def pop_first(self):
        if self.root is None:
            return None
        result = self.root.value
        self.root = self.root.next
        if self.root:
            self.root.prev = None
        else:
            self.tail = None  # Список стал пустым
        self.size -= 1
        return result
    # return True if elem in list
    def find(self,value):
        runner = self.root
        while runner is not None:
            if runner.value == value:
                return True
            runner = runner.next
        return False
    # return elements of list
    def display(self):
        runner = self.root
        elements = []
        while runner:
            elements.append(runner.value)
            runner = runner.next
        return elements
    # return reverse elements of list
    def reverse(self):
        runner = self.tail
        elements = []
        while runner:
            elements.append(runner.value)
            runner = runner.prev
        return elements


import unittest

class TestDoubleLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoubleLinkedList()

    def test_append(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.display(), [1, 2, 3])
        self.assertEqual(self.dll.reverse(), [3, 2, 1])

    def test_prepend(self):
        self.dll.prepend(1)
        self.dll.prepend(2)
        self.dll.prepend(3)
        self.assertEqual(self.dll.display(), [3, 2, 1])
        self.assertEqual(self.dll.reverse(), [1, 2, 3])

    def test_insert(self):
        self.dll.append(1)
        self.dll.append(3)
        self.dll.insert(1, 2)  # Вставляем 2 между 1 и 3
        self.assertEqual(self.dll.display(), [1, 2, 3])

    def test_remove(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.dll.remove(2)
        self.assertEqual(self.dll.display(), [1, 3])
        self.dll.remove(1)
        self.assertEqual(self.dll.display(), [3])
        self.dll.remove(3)
        self.assertEqual(self.dll.display(), [])

    def test_pop(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.pop(), 3)
        self.assertEqual(self.dll.display(), [1, 2])
        self.assertEqual(self.dll.pop(), 2)
        self.assertEqual(self.dll.pop(), 1)
        self.assertEqual(self.dll.pop(), None)

    def test_pop_first(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.pop_first(), 1)
        self.assertEqual(self.dll.display(), [2, 3])
        self.assertEqual(self.dll.pop_first(), 2)
        self.assertEqual(self.dll.pop_first(), 3)
        self.assertEqual(self.dll.pop_first(), None)

    def test_find(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertTrue(self.dll.find(2))
        self.assertFalse(self.dll.find(4))

    def test_display(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.display(), [1, 2, 3])

    def test_reverse(self):
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.reverse(), [3, 2, 1])

if __name__ == '__main__':
    unittest.main()


"""
an 9 tests in 0.003s


OK

Process finished with exit code 0
"""