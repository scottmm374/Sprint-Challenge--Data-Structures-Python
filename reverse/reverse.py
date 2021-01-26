class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        output = " "
        current = self.head
        while current is not None:
            output += f'{current.value} ->'
            current = current.next_node

        return output

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev=None):
        if self.head is None:
            return None
        prev = prev
        node = self.head
        tracker = node.next_node

        while node:
            node.next_node = prev
            prev = node
            node = tracker

            if tracker is not None:
                tracker = tracker.next_node
        self.head = prev
