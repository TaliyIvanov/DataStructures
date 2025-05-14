"""

"""


class HashTableOnLists:

    # конструктор класса
    def __init__(self, capacity = 10):
        self._capacity = capacity
        self._size = 0
        # список списков
        self.array = [[] for _ in range(self._capacity)]

    # примитивная функция для создания хэшей
    # присваивает хэш равный остатку от значения self._capacity
    def _hash(self, key):
        return hash(key) % self._capacity

    # находит и возвращает элемент по ключу
    def find(self, key):
        index = self._hash(key)
        bucket = self.array[index]
        for k in bucket:
            if k == key:
                return k
        return None

    # вставляет элемент (условно масштабирует)
    def push(self, key):
        index = self._hash(key)
        bucket = self.array[index]
        if key not in bucket:
            bucket.append(key)
            self._size += 1
            if self._size > self._capacity * 0.75:
                self._resize()
        else:
            print(f'{key} есть в таблице.')

    # удаляет и возвращает элемент
    def pop(self, key):
        index = self._hash(key)
        bucket = self.array[index]
        if key in bucket:
            bucket.remove(key)
            self._size -= 1
            return key
        else:
            return None

    # Приватный вспомогательный метод для изменения размера внутреннего массива.
    def _resize(self):
        old_array = self.array
        self._capacity *= 2
        self.array = [[] for _ in range(self._capacity)]
        self._size = 0 # пересчитываем размер заново
        for bucket in old_array:
            for key in bucket:
                self.push(key)

    # Строковое представление объекта HashTableOnLists
    def __str__(self):
        return str(self.array)

# Тесты
import unittest

class TestHashTableOnLists(unittest.TestCase):
    def setUp(self):
        self.table = HashTableOnLists()

    def test_push_and_find(self):
        self.table.push("apple")
        self.table.push("banana")
        self.assertEqual(self.table.find("apple"), "apple")
        self.assertEqual(self.table.find("banana"), "banana")
        self.assertIsNone(self.table.find("orange"))

    def test_no_duplicates(self):
        self.table.push("apple")
        self.table.push("apple")  # вторая вставка не должна увеличить размер
        self.assertEqual(self.table._size, 1)
        self.assertEqual(self.table.find("apple"), "apple")

    def test_pop_existing(self):
        self.table.push("apple")
        result = self.table.pop("apple")
        self.assertEqual(result, "apple")
        self.assertIsNone(self.table.find("apple"))
        self.assertEqual(self.table._size, 0)

    def test_pop_non_existing(self):
        result = self.table.pop("nonexistent")
        self.assertIsNone(result)

    def test_resize(self):
        for i in range(20):  # должно триггернуть resize
            self.table.push(f"key{i}")
        self.assertGreaterEqual(self.table._capacity, 20)
        for i in range(20):
            self.assertEqual(self.table.find(f"key{i}"), f"key{i}")

    def test_table_structure_after_operations(self):
        self.table.push("apple")
        self.table.push("banana")
        self.table.pop("apple")
        structure = str(self.table)
        self.assertIn("banana", structure)
        self.assertNotIn("apple", structure)

if __name__ == "__main__":
    unittest.main()


"""
Ran 6 tests in 0.003s

OK

Process finished with exit code 0
"""


# Закоментированный код для лучшего понимания и повторения.

class HashTableOnLists:
    """
    Класс реализует хэш-таблицу с использованием метода цепочек (списков)
    для разрешения коллизий. Каждый элемент хэш-таблицы является списком,
    в котором хранятся ключи с одинаковым хэш-значением.
    """

    def __init__(self, capacity=10):
        """
        Инициализатор класса (конструктор).

        Args:
            capacity (int): Начальная емкость хэш-таблицы (количество "корзин").
                            По умолчанию равно 10.
        """
        # Сохраняем заданную емкость. Емкость определяет размер внутреннего массива.
        self._capacity = capacity
        # Инициализируем счетчик количества элементов в таблице нулем.
        self._size = 0
        # Создаем основной массив (список), где каждый элемент - это пустой список.
        # Эти вложенные списки будут "корзинами" или "цепочками" для хранения ключей.
        # Длина основного массива равна заданной емкости (_capacity).
        self.array = [[] for _ in range(self._capacity)]

    def _hash(self, key):
        """
        Приватный метод для вычисления хэш-значения ключа.
        Определяет индекс "корзины" в массиве `self.array`,
        в которую должен попасть ключ.

        Args:
            key: Ключ, для которого вычисляется хэш. Должен быть хэшируемым типом.

        Returns:
            int: Индекс корзины (от 0 до self._capacity - 1).
        """
        # Используем встроенную функцию hash() для получения хэш-кода ключа.
        # Затем берем остаток от деления на текущую емкость (_capacity),
        # чтобы получить индекс в пределах размера нашего массива.
        return hash(key) % self._capacity

    def find(self, key):
        """
        Метод для поиска ключа в хэш-таблице.

        Args:
            key: Ключ, который нужно найти.

        Returns:
            Найденный ключ, если он существует в таблице, иначе None.
        """
        # 1. Вычисляем индекс корзины, где мог бы находиться ключ.
        index = self._hash(key)
        # 2. Получаем саму корзину (список) по вычисленному индексу.
        bucket = self.array[index]
        # 3. Проходим по всем элементам (ключам) в найденной корзине.
        for k in bucket:
            # 4. Если находим искомый ключ...
            if k == key:
                # ...возвращаем его.
                return k
        # 5. Если мы прошли всю корзину и не нашли ключ, значит его нет в таблице.
        return None

    def push(self, key):
        """
        Метод для вставки ключа в хэш-таблицу.
        Если ключ уже существует, он не добавляется повторно (выводится сообщение).
        Также метод проверяет коэффициент загрузки и при необходимости
        увеличивает размер таблицы (рехэширование).

        Args:
            key: Ключ, который нужно вставить.
        """
        # 1. Вычисляем индекс корзины для ключа.
        index = self._hash(key)
        # 2. Получаем корзину по индексу.
        bucket = self.array[index]
        # 3. Проверяем, нет ли уже такого ключа в этой корзине.
        if key not in bucket:
            # 4. Если ключа нет, добавляем его в конец списка (цепочки) этой корзины.
            bucket.append(key)
            # 5. Увеличиваем счетчик общего количества элементов в таблице.
            self._size += 1
            # 6. Проверяем коэффициент загрузки (load factor).
            # Коэффициент загрузки = _size / _capacity
            # Если он превышает 0.75 (75%), это значит, что таблица становится
            # слишком заполненной, и операции могут замедлиться из-за длинных цепочек.
            if self._size > self._capacity * 0.75:
                # 7. Если превышен порог, вызываем приватный метод _resize()
                # для увеличения емкости таблицы и перераспределения элементов.
                self._resize()
        else:
            # Если ключ уже существует в корзине, сообщаем об этом.
            # В реальных хэш-таблицах (как dict в Python) здесь могло бы
            # происходить обновление значения, связанного с ключом.
            print(f'Ключ "{key}" уже есть в таблице.')

    def pop(self, key):
        """
        Метод для удаления ключа из хэш-таблицы.

        Args:
            key: Ключ, который нужно удалить.

        Returns:
            Удаленный ключ, если он был найден и удален, иначе None.
        """
        # 1. Вычисляем индекс корзины, где должен находиться ключ.
        index = self._hash(key)
        # 2. Получаем корзину по индексу.
        bucket = self.array[index]
        # 3. Проверяем, есть ли ключ в этой корзине.
        if key in bucket:
            # 4. Если есть, удаляем его из списка корзины.
            bucket.remove(key)
            # 5. Уменьшаем счетчик общего количества элементов.
            self._size -= 1
            # 6. Возвращаем удаленный ключ.
            return key
        else:
            # 7. Если ключ не найден в корзине, возвращаем None.
            return None

    def _resize(self):
        """
        Приватный вспомогательный метод для увеличения размера хэш-таблицы (рехэширования).
        Вызывается, когда коэффициент загрузки превышает пороговое значение (0.75).
        Создает новый массив большего размера и переносит в него все существующие элементы,
        пересчитывая их хэши с учетом новой емкости.
        """
        # 1. Сохраняем ссылку на текущий (старый) массив данных.
        old_array = self.array
        # 2. Увеличиваем емкость таблицы (обычно удваивают).
        self._capacity *= 2
        # 3. Создаем новый, пустой массив увеличенного размера с новой емкостью.
        self.array = [[] for _ in range(self._capacity)]
        # 4. Сбрасываем счетчик размера. Метод push сам корректно посчитает
        #    количество элементов при их повторной вставке.
        self._size = 0
        # 5. Проходим по каждой корзине старого массива.
        for bucket in old_array:
            # 6. Проходим по каждому ключу в текущей старой корзине.
            for key in bucket:
                # 7. Вставляем ключ в *новую* таблицу с помощью метода push.
                #    Важно: `push` внутри себя вызовет `_hash`, который теперь
                #    использует *новую* `_capacity`, поэтому ключ попадет
                #    в правильную корзину *нового* массива. `push` также
                #    обновит `_size`.
                self.push(key)
        # print(f"Таблица увеличена, новая емкость: {self._capacity}") # Для отладки

    def __str__(self):
        """
        Метод для получения строкового представления хэш-таблицы.
        Возвращает строковое представление внутреннего массива списков.
        Полезен для отладки и визуализации содержимого таблицы.

        Returns:
            str: Строковое представление объекта HashTableOnLists.
        """
        return str(self.array)


"""

**Ключевые моменты, на которые стоит обратить внимание при изучении:**

1.  **Хэш-функция (`_hash`)**: Как она преобразует ключ в индекс массива. Почему важен оператор `% self._capacity`? (Чтобы индекс был в пределах массива).
2.  **Коллизии**: Что происходит, если `_hash` выдает одинаковый индекс для разных ключей? (Ключи добавляются в один и тот же вложенный список - "цепочку"). Как `find`, `push`, `pop` работают с этими цепочками? (Они итерируют по списку в нужной корзине).
3.  **Метод цепочек**: Это и есть использование списков (`self.array[index]`) для хранения элементов с одинаковым хэшем.
4.  **Коэффициент загрузки (Load Factor)**: Зачем он нужен (`_size / _capacity`)? (Чтобы избежать слишком длинных цепочек, которые замедляют поиск/вставку/удаление). Как он используется в `push`? (Для запуска `_resize`).
5.  **Рехэширование (`_resize`)**: Почему просто скопировать старый массив в новый, больший, нельзя? (Потому что изменилась `_capacity`, и остаток от деления `% self._capacity` будет другим, ключи должны попасть в *новые* корзины). Как элементы переносятся? (Каждый элемент из старой таблицы заново вставляется (`push`) в новую таблицу).
6.  **Амортизированная сложность**: Хотя `_resize` может быть долгой операцией (O(N), где N - количество элементов), она происходит редко. В среднем операции `push`, `find`, `pop` выполняются за O(1 + k), где k - средняя длина цепочки. При хорошем хэшировании и контроле коэффициента загрузки k близко к константе, и операции считаются амортизированно O(1).
"""