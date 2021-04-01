def binary_search(sorted_list, target):
    if not sorted_list:
        return 'value not found'
    mid_idx = len(sorted_list)//2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx


# base case for when we DO find the value.
sorted_values = [13, 14, 15, 16, 17]
print(binary_search([], 42))
print(binary_search(sorted_values, 42))
print(binary_search(sorted_values, 15))