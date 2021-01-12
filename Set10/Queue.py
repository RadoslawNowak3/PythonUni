class Queue:

    def __init__(self, elements=None, size=5):
        self.n = size + 1
        self.items = self.n * [None]
        self.head = 0
        self.tail = 0
        if elements is not None:
            i=0
            for element in elements:
                self.items[i]=element
                i+=1
            self.tail = i

    def __str__(self):
        return str(self.items)

    def __eq__(self, other):
        return self.items == other.items

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if(self.is_full()==True):
            raise OverflowError("Queue is full")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if(self.is_empty()):
            raise ValueError("Queue is empty")
        data = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.n
        return data
