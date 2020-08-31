class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.tail = 0
        self.head = 0
        self.size = 0

    def append(self, item):
        if self.size < self.capacity:
            self.data.append(item)
            self.tail = (self.tail + 1) % self.capacity
            self.size = self.size + 1

            self.head = (self.head + 1) % self.capacity

        else:
            self.head = (self.head + 1) % self.capacity
            self.data.append(item)
            self.tail = (self.tail + 1) % self.capacity

    def get(self):
        if self.size == 0:
            print("Queue is empty")
            return None
        else:
            curr = self.head

            for curr in range(self.size):
                print("Value", self.data[curr])
                curr = (curr + 1) % self.capacity
                print(curr)


buffer = RingBuffer(5)
buffer.get()

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
print("at max")
buffer.get()
buffer.append("f")
print("after max")
buffer.get()
