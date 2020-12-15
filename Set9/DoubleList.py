class Node:
    """Klasa reprezentująca węzeł listy dwukierunkowej."""
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data
class DoubleList:
    """Klasa reprezentująca całą listę dwukierunkową."""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __str__(self):
        result = ''
        current = self.head
        while current is not None:
            result += (',' + str(current))
            current = current.next
        result = '[' + result[1:] + ']'
        return result

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node     # stary head
            self.head = node          # nowy head
        else:         # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.tail:
            node.prev = self.tail
            self.tail.next = node     # stary tail
            self.tail = node          # nowy tail
        else:         # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def remove_head(self):   # zwraca node
        if self.is_empty():
            raise ValueError("Empty list")
        elif self.head is self.tail:   # length == 1
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.head
            self.head = self.head.next
            self.head.prev = None   # czyszczenie
            node.next = None   # czyszczenie
            self.length -= 1
            return node

    def remove_tail(self):   # zwraca node
        if self.is_empty():
            raise ValueError("Empty list")
        elif self.head is self.tail:   # length == 1
            node = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None   # czyszczenie
            node.prev = None
            self.length -= 1
            return node

    def find_max(self):
        current = self.head
        max_node = current
        while current.next is not None:
            current = current.next
            if current > max_node:
                max_node = current
        return max_node

    # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.
    def find_min(self):
        current = self.head
        min_node = current
        while current.next is not None:
            current = current.next
            if current < min_node:
                min_node = current
        return min_node

        # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.

    def remove(self, node):
        if self.is_empty():
            raise ValueError("Empty list")
        elif node == self.head:
            self.remove_head()
        elif node == self.tail:
            self.remove_tail()
        else:
            current = self.head
            while current.next is not None and current != node:
                current = current.next
            if(current == node):
                previous_node = current.prev
                previous_node.next = current.next
                next_node = current.next
                next_node.prev = previous_node

        # Usuwa wskazany węzeł z listy.

    def clear(self):
        if self.is_empty():
            raise ValueError("Empty list")
        current = self.tail
        self.tail = None
        while current.prev is not None:
             current = current.prev
             current.next.data = None
             current.next.prev = None
        current.next = None
        self.head.data = None
        self.head = None