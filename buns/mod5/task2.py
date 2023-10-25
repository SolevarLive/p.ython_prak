
class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is None:
            return None
        val = self.start.data
        if self.start.nref is None:
            self.start = None
            self.end = None
        else:
            self.start = self.start.nref
            self.start.pref = None
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        new_node = Node(val)
        if n == 0:
            if self.start is None:
                self.start = new_node
                self.end = new_node
            else:
                new_node.nref = self.start
                self.start.pref = new_node
                self.start = new_node
        else:
            current = self.start
            for i in range(n - 1):
                if current is None:
                    return
                current = current.nref
            if current is None:
                return
            new_node.nref = current.nref
            new_node.pref = current
            if current.nref is not None:
                current.nref.pref = new_node
            current.nref = new_node

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        current = self.start
        while current is not None:
            print(current.data)
            current = current.nref