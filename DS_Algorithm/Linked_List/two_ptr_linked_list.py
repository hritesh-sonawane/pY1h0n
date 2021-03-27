from linked_list import LinkedList

def nth_last_node(linked_list, n):
    current = None
    tail_seeker = linked_list.head_node
    count = 1

    while tail_seeker:
        tail_seeker = tail_seeker.get_next_node()
        count += 1

        if count >= n + 2:
            if current is None:
                current = linked_list.head_node
            else:
                current = current.get_next_node()
    return current    

def generate_test_linked_list():
    ll = LinkedList()
    for i in range(20, 0, -1):
        ll.insert_beginning(i)
    return ll


test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)

# egs: obtain the 2nd to last node of any linked list.
# T -> tail pointer
# N -> nth_last pointer

# Starting State
# count = 1
# T
# 1  2  3  4  5

# First Tick
# count = 2
#    T
# 1  2  3  4  5

# Second Tick
# count = 3
#       T
# N
# 1  2  3  4  5

# Third Tick
# count = 4
#          T
#    N
# 1  2  3  4  5

# Fourth Tick
# count = 5
#             T
#       N
# 1  2  3  4  5

# Final Tick
# count = 6
#                T
#          N
# 1  2  3  4  5  None


# Time Complexity: O(n) : We must iterate through the entire list once
# Space Complexity: O(1) : We always use only three variables no matter what size the linked list is: two pointers and a counter

# Pointers at different speeds
# egs: Find middle element of linked list
# 2 pointers: fast and slow. For every 2 steps fast takes, slow takes 1

# def find_middle(linked_list):
#     count = 0
#     fast = linked_list.head_node
#     slow = linked_list.head_node

#     while fast:
#             fast = fast.get_next_node()
#             if count % 2 != 0:
#                 slow = slow.get_next_node()
#                 count += 1
#     return slow