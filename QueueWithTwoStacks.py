"""
Здесь будет реализована очередь с использованием двух стэков.
Идея интересная и эффективная.
Этот метод реализует очередь через два стека, эффективно поддерживая операции добавления и удаления.

### **Пояснения по методам `QueueWithTwoStacks`**

1. **`__init__()`**
   - Создает два стека:
     - `stack1` — для добавления новых элементов.
     - `stack2` — для удаления элементов.

2. **`enqueue(x)`**
   - Добавляет элемент `x` в `stack1`.
   - Работает за **O(1)**.

3. **`dequeue()`**
   - Если `stack2` пуст, перекладывает все элементы из `stack1` в `stack2` (реверс порядка).
   - Удаляет и возвращает верхний элемент `stack2` (первый в очереди).
   - Если оба стека пусты, выбрасывает `IndexError`.
   - Амортизированная сложность **O(1)**, в худшем случае **O(n)**.

4. **`front()`**
   - Работает аналогично `dequeue()`, но просто возвращает верхний элемент `stack2` без удаления.
   - Если очередь пуста, выбрасывает `IndexError`.
   - Амортизированная сложность **O(1)**, в худшем случае **O(n)**.

5. **`is_empty()`**
   - Возвращает `True`, если оба стека пусты.
   - Сложность **O(1)**.

6. **`size()`**
   - Возвращает суммарное количество элементов в обоих стеках.
   - Сложность **O(1)**.
"""


class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, x):
        self.stack1.append(x)
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Queue is empty")
        return self.stack2.pop()
    def front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Queue is empty")
        return self.stack2[-1]
    def is_empty(self):
        return not (self.stack1 or self.stack2)
    def size(self):
        return len(self.stack1) + len(self.stack2)

import unittest

class TestQueueWithTwoStacks(unittest.TestCase):
    def setUp(self):
        self.queue = QueueWithTwoStacks()

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
        self.assertEqual(str(context.exception), 'Queue is empty')

    def test_front(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.front(), 10)
        self.assertEqual(self.queue.size(), 2)  # Проверяем, что элемент не удалился

    def test_front_from_empty_queue(self):
        with self.assertRaises(IndexError) as context:
            self.queue.front()
        self.assertEqual(str(context.exception), 'Queue is empty')

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
Ran 7 tests in 0.003s

OK

Кстати забавное наблюдение, эти 7 тестов выполнились шустрее на 0.001s, чем у очереди на списке и на deque
"""