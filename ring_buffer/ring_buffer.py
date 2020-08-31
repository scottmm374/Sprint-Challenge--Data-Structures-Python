class RingBuffer:
    def __init__(self, capacity, next=None):
        self.capacity = 5
        self.data = []
        self.tail = -1
        self.head = 0
        self.size = 0

    def append(self, item):
        pass

    def get(self):
        if self.size == 0:
            print("Queue is empty")
            return None
        else:
            curr = self.head

            for curr in range(self.size):
                curr = (curr + 1) % self.capacity
