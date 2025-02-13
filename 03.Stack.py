"""
В процессе изучения и разработки
"""
class MyStack():
    def __init__(self):
        self._stack = []
    def push(self, item):
        self._stack.append(item)
    def pop(self):
        self._stack = self._stack[:-1]
    def top(self):
        return self._stack[-1]
    def is_empty(self):
        if self._stack :
            return True
        else:
            return False

def Main():
    pass