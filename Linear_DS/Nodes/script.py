class Node:

    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    # getter
    def get_value(self):
        return self.value
  
    # getter
    def get_link_node(self):
        return self.link_node

    # setter
    def set_link_node(self, link_node):
        self.link_node = link_node


node1 = Node("apple")
node2 = Node("banana")
node3 = Node("kiwi")

node2.set_link_node(node1)
node3.set_link_node(node2)
# 1 -> 2 -> 3

node1_data = node2.get_link_node().get_value()
node2_data = node3.get_link_node().get_value()

print(node1_data)
# apple
print(node2_data)
# banana