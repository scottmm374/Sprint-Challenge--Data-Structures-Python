class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.head = 0

    def append(self, item):
        # if Que is full
        if len(self.data) == self.capacity:
            # item equal to current head
            self.data[self.head] = item
        # Increment head to next index (New oldest Item)
            self.head = (self.head + 1) % self.capacity

        # If Que is not full Append new Item
        else:
            self.data.append(item)

    def get(self):
        if len(self.data) == 0:
            print("Queue is empty")
            return None
        else:
            print(self.data)
            return self.data


buffer = RingBuffer(3)
# buffer.get()

buffer.append('a')
buffer.append('b')
buffer.append('c')
# print("max")
buffer.get()
buffer.append('d')
buffer.get()
buffer.append('e')
# print("replace two")
buffer.get()
buffer.append("f")
buffer.get()
buffer.append("g")
# print("after max")
buffer.get()
