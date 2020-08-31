class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        # self.tail = 0
        self.head = 0
        self.size = 0

    def append(self, item):
        if self.size == self.capacity:
            data = self.data[self.head]
            self.data.remove(data)
            self.head = (self.head + 1) % self.capacity
            self.size = self.size - 1
            # return data
            return self.append(item)
        else:
            self.data.append(item)
            self.size = self.size + 1

    # def append(self, item):
    #     if self.size() == self.capacity-1:
    #         return None
    #     self.data.append(item)
    #     self.tail = (self.tail + 1) % self.capacity
    #     # self.size = self.size + 1
    #     return True

    # def dequeue(self):
    #     if self.size() == 0:
    #         return ("Queue Empty!")
    #     data = self.data[self.head]
    #     # self.size = self.size - 1
    #     self.head = (self.head + 1) % self.capacity
    #     return data

    # Calculating the size of the queue

    # def size(self):
    #     if self.tail >= self.head:
    #         return (self.tail-self.head)
    #     return (self.capacity - (self.head-self.tail))

    def get(self):
        if self.size == 0:
            print("Queue is empty")
            return None
        else:
            print(self.data)
            return self.data
            # curr = self.head

            # for curr in range(self.size):
            #     print("Value", self.data[curr])
            #     curr = (curr + 1) % self.capacity
            #     print(curr)
            # return self.data[curr]


buffer = RingBuffer(3)
# buffer.get()

buffer.append('a')
buffer.append('b')
buffer.append('c')
# print("max")
buffer.get()
buffer.append('d')
buffer.append('e')
# print("replace two")
# buffer.get()
buffer.append("f")
buffer.append("g")
# print("after max")
# buffer.get()
