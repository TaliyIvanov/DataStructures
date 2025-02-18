"""
### Определение
Односвязный список (иногда «связный список») — базовая структура данных,
представляющая собой соединённые узлы с однотипными данными.
Каждый узел состоит из элемента и ссылки на следующий элемент.

Самый первый элемент списка называют головой (head) односвязного списка,
а последний — хвостом (tail). Последний элемент односвязного списка в качестве ссылки
содержит null-значение.
### Особенности
В отличие от классического массива, где данные в памяти расположены строго последовательно,
в односвязном списке, наоборот, данные расположены хаотично и связывание узлов списка
происходит посредством ссылок. За счёт этой особенности в односвязный список можно добавлять
произвольное число элементов, однако, доступ будет осуществляться только последовательно.
Произвольного доступа к элементам в односвязном списке нет.

#### **Описание класса `MyLinkedList`**

##### **Как работает класс?**
Класс `MyLinkedList` реализует односвязный список, где каждый элемент (`Node`) хранит значение
(`value`) и ссылку на следующий элемент (`next`).
Список управляется через атрибут `self.root`, который указывает на первый элемент списка.

##### **Структура данных**
- **Класс `Node`**: узел списка, содержащий `value` и `next`.
- **Атрибут `self.root`**: хранит ссылку на первый элемент списка (`None`, если список пуст).
- **Методы**: позволяют добавлять, удалять, искать элементы и считать их количество.
"""

from markdown_it.rules_core.normalize import NULL_RE
import unittest

class MyLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.root = None

    # Проверка на наличие элемента в списке
    def find(self, value):
        runner = self.root
        while runner is not None:
            if runner.value == value:
                return True
            runner = runner.next
        return False # Элемент не найден
    # подсчет кол-ва элементов
    def count(self):
        counter = 0
        runner = self.root
        while runner is not None:
            counter += 1
            runner = runner.next
        return counter

    # Добавить в конец
    def push_back(self, elem):
        new_node = self.Node(elem)
        if self.root is None:  # Case: Empty list
            self.root = new_node
            return
        runner = self.root
        while runner.next is not None:   # Traverse to last node
            runner = runner.next
        runner.next = new_node  # Append new node at the end
    # Добавить в начало
    def push_front(self, elem):
        new_node = self.Node(elem)
        new_node.next = self.root
        self.root = new_node
    # Удалить первый
    def pop_front(self):
        if self.root is None:  # Проверка на пустой список
            return
        self.root = self.root.next  # Сдвигаем голову списка

    # Remove last elem
    def pop_back(self):
        runner = self.root
        if runner is None:  # Case: Empty list
            raise ValueError("List is empty")
        if runner.next is None:  # Case: Only one element
            self.root = None  # Удаляем единственный элемент
            return
        while runner.next.next is not None:  # Ищем предпоследний узел
            runner = runner.next
        runner.next = None  # Удаляем последний узел

# протестируем класс

class TestMyLinkedList(unittest.TestCase):
    def setUp(self):
        """Запускается перед каждым тестом"""
        self.lst = MyLinkedList()

    def test_push_front(self):
        self.lst.push_front(10)
        self.assertEqual(self.lst.root.value, 10)

        self.lst.push_front(20)
        self.assertEqual(self.lst.root.value, 20)
        self.assertEqual(self.lst.root.next.value, 10)

    def test_push_back(self):
        self.lst.push_back(30)
        self.assertEqual(self.lst.root.value, 30)

        self.lst.push_back(40)
        self.assertEqual(self.lst.root.next.value, 40)

    def test_pop_front(self):
        self.lst.push_front(50)
        self.lst.push_front(60)
        self.lst.pop_front()

        self.assertEqual(self.lst.root.value, 50)

        self.lst.pop_front()
        self.assertIsNone(self.lst.root)

    def test_pop_back(self):
        self.lst.push_back(70)
        self.lst.push_back(80)
        self.lst.pop_back()

        self.assertEqual(self.lst.root.value, 70)
        self.assertIsNone(self.lst.root.next)

        self.lst.pop_back()
        self.assertIsNone(self.lst.root)

    def test_find(self):
        self.lst.push_back(90)
        self.lst.push_back(100)
        self.assertTrue(self.lst.find(90))
        self.assertTrue(self.lst.find(100))
        self.assertFalse(self.lst.find(110))

    def test_count(self):
        self.assertEqual(self.lst.count(), 0)

        self.lst.push_back(120)
        self.assertEqual(self.lst.count(), 1)

        self.lst.push_back(130)
        self.assertEqual(self.lst.count(), 2)

        self.lst.pop_front()
        self.assertEqual(self.lst.count(), 1)

        self.lst.pop_back()
        self.assertEqual(self.lst.count(), 0)

    def test_pop_back_empty_list(self):
        with self.assertRaises(ValueError):
            self.lst.pop_back()

if __name__ == '__main__':
    unittest.main()
