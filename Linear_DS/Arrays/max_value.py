# Find and return the max value in the list
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

# Linear Search Algorithm
def linear_search(search_list):
    max_score_index = None

    for idx in range(len(search_list)):
        if not max_score_index or search_list[idx] > search_list[max_score_index]:
            max_score_index = idx
    return search_list[max_score_index]


highest_score = linear_search(test_scores)
print(highest_score)