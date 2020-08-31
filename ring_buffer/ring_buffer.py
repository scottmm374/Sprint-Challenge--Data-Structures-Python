class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.tail = -1
        self.head = 0
        self.size = 0

    def append(self, item):
        if self.size < self.capacity:
            item = self.data[self.head]
            print(item)
            self.head = (self.head + 1) % self.capacity

            return item

        else:

            self.tail = (self.tail + 1) % self.capacity
            self.data[self.tail] = item
            self.size = self.size + 1

    def get(self):
        if self.size == 0:
            print("Queue is empty")
            return None
        else:
            curr = self.head

            for curr in range(self.size):
                curr = (curr + 1) % self.capacity


buffer = RingBuffer(5)
buffer.get()

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.get()
