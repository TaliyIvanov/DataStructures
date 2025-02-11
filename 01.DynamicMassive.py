"""
Реализуйте класс динамический массив, имеющий методы:
- push_back(element) - Добавляет элемент в конец массива. Работает амортизировано за O(1)
- pop_back() - Удаляет элемент, находящийся в конце массива, а также возвращающий значение удаленного элемента
- size() - Возвращает количество элементов в массиве.
- capacity() - Возвращает число элементов, которое массив может содержать без выделения дополнительного пространства.

Также должен быть реализован метод взятия и изменения элемента по индексу - по [] - как у стандартного массива.
"""

class MyDynamicArray:
    def __init__(self):
        self.size = 0 # кол-во элементов в массиве
        self.capacity = 1 # начальная емкость массива
        self.array = [None] * self.capacity

    def size(self):
        return self.size

    def capacity(self):
        return self.capacity

    def push_back(self, item):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = item
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise IndexError("Cannot pop from empty array")
        item = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return item

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def __setitem__(self, index, value):
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")
        self.array[index] = value

def process_commands():
    arr = DynamicArray()
    n = int(input())
    for _ in range(n):
        command = input().strip()
        if command == "push_back":
            value = int(input())
            arr.push_back(value)
        elif command == "pop_back":
            print(arr.pop_back())
        elif command == "size":
            print(arr.size())
        elif command == "index":
            index = int(input())
            print(arr[index])


if __name__ == "__main__":
    process_commands()
