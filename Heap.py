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
import math

class MinHeap():
    def __init__(self):
        self.heap = []

    def FindMin(self):
        return self.heap[0]
    def ShiftUP(self, i):
        parent = math.floor((i-1)/2)
        pass
    def ShiftDown:
        pass
    def GetMax(self):
        return self.heap[-1]
    def PopMax(self):
        pass
    def Push(self, value):
        pass
    def MakeHeap(self, arr):
        pass
    def IsEmpty(self):
        if len(self.heap) == 0:
            return True