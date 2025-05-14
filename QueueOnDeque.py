"""
Ровно все тоже самое, что и с очередью на списке, но эффективнее

- `append()` и `popleft()` работают за **O(1)**
- `list.pop(0)` работал бы за **O(n)** (неэффективно)

`collections.deque` — это двусторонняя очередь (double-ended queue) в Python,
оптимизированная для быстрых операций вставки и удаления с обоих концов (O(1) вместо O(n) у списка).
"""

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    # Добавляет элемент в конец очереди
    def enqueue(self, item):
        self.queue.append(item)
    # Удаляет и возвращает первый элемент очереди
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty stack")
        return self.queue.popleft()
    # Возвращает первый элемент без удаления
    def front(self):
        if self.is_empty():
            raise IndexError("front from empty stack")
        return self.queue[0]
    # Проверяет, пуста ли очередь
    def is_empty(self):
        return len(self.queue) == 0
    # Возвращает количество элементов в очереди
    def size(self):
        return len(self.queue)

import unittest

class TestSimpleQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        self.assertFalse(self.queue.is_empty())

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertTrue(self.queue.is_empty())

    def test_dequeue_from_empty_queue(self):
        with self.assertRaises(IndexError) as context:
            self.queue.dequeue()
        self.assertEqual(str(context.exception), 'dequeue from empty stack')

    def test_front(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.front(), 10)
        self.assertEqual(self.queue.size(), 2)  # Проверяем, что элемент не удалился

    def test_front_from_empty_queue(self):
        with self.assertRaises(IndexError) as context:
            self.queue.front()
        self.assertEqual(str(context.exception), 'front from empty stack')

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(5)
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 0)


if __name__ == '__main__':
    unittest.main()

"""
Ran 7 tests in 0.004s

OK
"""