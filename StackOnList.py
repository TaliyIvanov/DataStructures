"""
Стек (Stack) — это структура данных, работающая по принципу
**LIFO (Last In, First Out)**, то есть «последним
пришел — первым вышел». Представь его как стопку тарелок:
ты кладешь новую тарелку сверху, и именно ее берешь первой,
когда нужно убрать одну.

### Основные операции

1. **push(x)** — добавление элемента в стек (наверх).
2. **pop()** — удаление верхнего элемента.
3. **peek() / top()** — просмотр верхнего элемента без удаления.
4. **isEmpty()** — проверка, пуст ли стек.
5. **size()** — количество элементов в стеке.

### Реализация

Стек можно реализовать:

- **Список (Array/List)** – в языках вроде Python (list), Java (ArrayList) или C++ (vector).
- **Связанный список (Linked List)** – где каждый элемент содержит ссылку на следующий.
- **Двусторонняя очередь (Deque)** – эффективен в Python (`collections.deque`).

В данном файле реализуется стек на списке!
"""
class StackOnList():
    def __init__(self):
        self._stack = []
    # добавляет элемент в стэк
    def push(self, item):
        self._stack.append(item)
    # удаляет и возвращает верхний элемент стэка
    def pop(self):
        if not self.is_empty():
            return self._stack.pop()
        raise IndexError('pop from empty stack')
    # возвращает верхний элемент стека, не удаляя его
    def top(self):
        if not self.is_empty():
            return self._stack[-1]
        raise IndexError('top from empty stack')
    # Проверяет не пустой ли стэк
    def is_empty(self):
        return len(self._stack) == 0
    # возвращает размер стэка
    def size(self):
        return len(self._stack)


import unittest

class TestStackOnList(unittest.TestCase):
    def setUp(self):
        self.stack = StackOnList()

    def test_push(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.size(), 2)
        self.assertEqual(self.stack.top(), 20)

    def test_pop(self):
        self.stack.push(5)
        self.stack.push(15)
        self.assertEqual(self.stack.pop(), 15)  # Должен удалить и вернуть верхний элемент
        self.assertEqual(self.stack.size(), 1)

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.stack.pop()  # Должен выбросить ошибку

    def test_top(self):
        self.stack.push(42)
        self.assertEqual(self.stack.top(), 42)
        self.stack.push(99)
        self.assertEqual(self.stack.top(), 99)

    def test_top_empty(self):
        with self.assertRaises(IndexError):
            self.stack.top()  # Должен выбросить ошибку

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(3)
        self.stack.push(7)
        self.assertEqual(self.stack.size(), 2)

if __name__ == "__main__":
    unittest.main()


"""
Ran 7 tests in 0.003s

OK
"""