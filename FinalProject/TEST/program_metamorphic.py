def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    # Find the middle point and divide the unsorted list
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    
    return list(merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            del left_half[0]
        else:
            res.append(right_half[0])
            del right_half[0]
    if len(left_half) == 0:
        res += right_half
    else:
        res += left_half
    return res

def test_permutation_of_input_order():
    scenarios = [
        ([3, 1, 4, 2], [2, 4, 1, 3]),           # Basic permutation
        ([5, 3, 2, 1], [1, 2, 3, 5]),           # Sorted to reverse
        ([9, 6, 8, 7], [8, 7, 6, 9]),           # Random permutation
        ([1], [1]),                             # Single element
        ([], []),                               # Empty list
        ([3, 3, 2, 2], [2, 3, 3, 2]),           # List with duplicates
        ([1, 2, 3], [3, 2, 1]),                 # Full reversal
        ([10, -1, 0, 5], [0, 10, 5, -1]),       # Mixed integers
        ([4.1, 2.2, 3.3], [3.3, 4.1, 2.2]),     # Floating points
        ([1, 2, 2, 1], [2, 1, 1, 2])            # Repeated elements in mixed order
    ]
    
    for original, permuted in scenarios:
        assert merge_sort(original) == merge_sort(permuted), f"MR1 Failed: {original} != {permuted}"
    
    print("MR1 Passed: All scenarios for Permutation of Input Order are valid.")

def test_addition_of_duplicate_elements():
    scenarios = [
        ([2, 3, 1], [2, 3, 1, 2, 3]),          # Basic duplicates
        ([5, 5, 5], [5, 5, 5, 5, 5, 5]),       # All duplicates
        ([1, 2, 3], [1, 2, 3, 1, 2, 3]),       # Duplicates among sorted
        ([0], [0, 0]),                         # Single element
        ([], []),                              # Empty case
        ([4, 1, 4], [1, 4, 4, 4, 1]),          # Multiple duplicates in random order
        ([1, 2, 2], [2, 1, 2, 2]),             # Duplicate at different positions
        ([7, 7, 3, 3], [3, 3, 7, 7, 7]),       # Two pairs of duplicates
        ([1, 1, 1, 2], [1, 1, 1, 2, 1]),       # Duplicate testing with order variation
        ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5])  # Testing stability with heavy duplicates
    ]
    
    for original, with_duplicates in scenarios:
        assert merge_sort(original) == sorted(original), "MR2 Failed: Original sort failed"
        assert merge_sort(with_duplicates) == sorted(with_duplicates), "MR2 Failed: Addition of duplicates failed"
    
    print("MR2 Passed: All scenarios for Addition of Duplicate Elements are valid.")


def test_sorting_stability():
    scenarios = [
        ([(1, 'apple'), (2, 'banana'), (1, 'cherry')], [(1, 'apple'), (1, 'cherry'), (2, 'banana')]),                           # Same keys with different items (stability check)
        ([(1, 'x'), (1, 'y'), (2, 'a')], [(1, 'x'), (1, 'y'), (2, 'a')]),                                                       # Simple stability with letters
        ([(4, 'pear'), (2, 'banana'), (2, 'banana')], [(2, 'banana'), (2, 'banana'), (4, 'pear')]),                             # Two items with the same key and checking order stability
        ([(3, 'grape'), (2, 'mango'), (3, 'kiwi'), (4, 'orange')], [(2, 'mango'), (3, 'grape'), (3, 'kiwi'), (4, 'orange')]),   # More complex case with repeated keys
        ([(6, 'peach'), (6, 'plum'), (5, 'apple')], [(5, 'apple'), (6, 'peach'), (6, 'plum')]),                                 # Checking stability with numbers and letters
        ([(5, 'a'), (3, 'b'), (5, 'c')], [(3, 'b'), (5, 'a'), (5, 'c')]),                                                       # Multiple entries with the same key
        ([(4, 'blue'), (4, 'red'), (2, 'green'), (2, 'yellow')], [(2, 'green'), (2, 'yellow'), (4, 'blue'), (4, 'red')])        # Mixed stability with repeated items and numbers
    ]
    
    for original, expected in scenarios:
        assert merge_sort(original) == expected, f"MR3 Failed: Stability check failed for {original}"
    
    print("MR3 Passed: All scenarios for Sorting Stability are valid.")


unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
print("Sorted list:", merge_sort(unsorted_list))

# Run test cases for each metamorphic relation
test_permutation_of_input_order()
test_addition_of_duplicate_elements()
test_sorting_stability()
