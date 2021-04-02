from linked_list import LinkedList, Node

def swap_nodes(input_list, val1, val2):
    print(f'Swapping {val1} with {val2}')

    node1_prev = None
    node2_prev = None
    node1 = input_list.head_node
    node2 = input_list.head_node

    if val1 == val2:
        print("Elements are the same - no swap needed!")
        return
    
    while node1 is not None:
        if node1.get_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()

    while node2 is not None:
        if node2.get_value() == val2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()

    if (node1 is None or node2 is None):
        print("Swap not possible - one or more element not in the list!")
        return

    if node1_prev is None:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)

    if node2_prev is None:
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)

    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)


swap_ll = LinkedList()

for i in range(10):
    swap_ll.insert_beginning(i)

print(swap_ll.stringify_list())
swap_nodes(swap_ll, 1, 6)
print(swap_ll.stringify_list())


# Time Complexity
# The worst case for time complexity in swap_nodes() is if both while loops must iterate all the way through to the end (either if there are no matching nodes, or if the matching node is at the tail).
# This means that it has a linear big O runtime of O(n), since each while loop has a O(n) runtime, and constants are dropped.

# Space Complexity
# There are four new variables created in the function regardless of the input, which means that it has a constant space complexity of O(1).