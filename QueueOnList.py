"""
Очередь — это структура данных, работающая по принципу **FIFO (First-In, First-Out)**, то есть **первый вошел —
первый вышел**. Это означает, что элементы добавляются в конец очереди, а удаляются с ее начала.

Здесь рассмотрена не самая эффективная реализация на списке
Но так как я учусь, необходимо уметь и самому делать что топорное)

- `enqueue(x) → O(1)` (добавление в конец)
- `dequeue() → O(n)` (удаление из начала сдвигает все элементы)
- Использовать **неэффективно**, так как `pop(0)` делает копирование всех элементов.
"""

class SimpleQueue:
    def __init__(self):
        self.queue = []
    # Добавляет элемент в конце очереди
    def enqueue(self, x):
        self.queue.append(x)
    # Удаляет и возвращает первый элемент
    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue from empty stack')
        return self.queue.pop(0)
    # Возвращает первый элемент без удаления
    def front(self):
        if self.is_empty():
            raise IndexError('front from empty stack')
        return self.queue[0]
    # Проверяет пустая ли очередь
    def is_empty(self):
        return len(self.queue) == 0
    # Возвращает кол-во элементов
    def size(self):
        return len(self.queue)


import unittest

class TestSimpleQueue(unittest.TestCase):
    def setUp(self):
        self.queue = SimpleQueue()

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