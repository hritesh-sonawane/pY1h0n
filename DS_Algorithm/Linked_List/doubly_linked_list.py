class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
    
    # setter
    def set_next_node(self, next_node):
        self.next_node = next_node

    # getter
    def get_next_node(self):
        return self.next_node

    # setter
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    # getter
    def get_value(self):
        return self.value


class DoublyLinkedList:
    pass

