def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]: 
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

# Mutant generation
def mutate_merge_sort(arr, mutation):
    if mutation == 1:
        # Change comparison operator in merge
        return merge_sort_mutation_1(arr)
    elif mutation == 2:
        # Reverse merge condition
        return merge_sort_mutation_2(arr)
    elif mutation == 3:
        # Off-by-one in split index
        return merge_sort_mutation_3(arr)
    elif mutation == 4:
        # Wrong recursive call order
        return merge_sort_mutation_4(arr)
    elif mutation == 5:
        # Change base case condition
        return merge_sort_mutation_5(arr)
    elif mutation == 6:
        # Skip one side of recursion
        return merge_sort_mutation_6(arr)
    elif mutation == 7:
        # Modify merge loop termination
        return merge_sort_mutation_7(arr)
    elif mutation == 8:
        # Incorrect array appending
        return merge_sort_mutation_8(arr)
    elif mutation == 9:
        # Reverse recursion depth condition
        return merge_sort_mutation_9(arr)
    elif mutation == 10:
        # Skip element appending
        return merge_sort_mutation_10(arr)
    
    return merge_sort(arr)  

def merge_sort_mutation_1(arr):
    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:  # Mutated: changed < to > to reverse the order
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged
    return merge_sort(arr)

def merge_sort_mutation_2(arr):
    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] == right[j]:  # Mutated: only append equal elements
                merged.append(left[i])
                i += 1
                j += 1
            else:
                if left[i] < right[j]:  # Default comparison is preserved, but logic is flawed
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged
    return merge_sort(arr)

def merge_sort_mutation_3(arr):
    mid = len(arr) // 3  # Mutated: changed split index to one-third
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])  # May lead to incorrect merging
    return merge(left_half, right_half)

def merge_sort_mutation_4(arr):
    def merge_sort_recursive(arr):
        if len(arr) <= 1:  # Mutated: changed base case to <= 1
            return arr
        mid = len(arr) // 2
        left_half = merge_sort(arr[mid:])  # Call right half first
        right_half = merge_sort(arr[:mid])  # Then call left half
        return merge(left_half, right_half)
    return merge_sort_recursive(arr)

def merge_sort_mutation_5(arr):
    if len(arr) < 4:  # Mutated: changed base case condition to < 4
        return arr  # May cause incorrect behavior for small arrays
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge_sort_mutation_6(arr):
    mid = len(arr) // 2
    # Mutated: skip the recursive call for the left half
    left_half = arr[:mid]  # No recursive call on left half
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge_sort_mutation_7(arr):
    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(left[j])  # Mutated: incorrectly append right[j]
                j += 1
        while i < len(left):  # This loop is preserved
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged
    return merge_sort(arr)

def merge_sort_mutation_8(arr):
    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            merged.append(left[i])  # Mutated: incorrectly append left[i] every time
            i += 1  # No condition for j
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged
    return merge_sort(arr)

def merge_sort_mutation_9(arr):
    def merge_sort_recursive(arr):
        if len(arr) > 2:  # Mutated: changed base case to > 2
            return arr
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
        return merge(left_half, right_half)
    return merge_sort_recursive(arr)

def merge_sort_mutation_10(arr):
    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                i += 1  # Mutated: skip appending left[i] altogether
            else:
                merged.append(right[j])  # Always append right[j]
                j += 1
        return merged  # Missing remaining elements
    return merge(arr, [])

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            i += 1  # Mutated: skip appending left[i] altogether
        else:
            j += 1
    return merged

# Test cases
test_cases = [
    ([3, 1, 4, 1, 5], [1, 1, 3, 4, 5]),         # TC1 - Random order
    ([10, -1, 2, 5, 0], [-1, 0, 2, 5, 10]),      # TC2 - Mixed positive and negative
    ([5, 9, 2, 8, 7], [2, 5, 7, 8, 9]),          # TC3 - Random order
    ([4, 2, 3, 2, 4, 3], [2, 2, 3, 3, 4, 4]),    # TC4 - Non-unique elements
    ([1], [1]),                                   # TC5 - Single element
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),           # TC6 - Reverse sorted
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),           # TC7 - Already sorted
    ([2, 2, 2, 2, 2], [2, 2, 2, 2, 2]),           # TC8 - All identical elements
    ([1, 3, 2, 3, 1], [1, 1, 2, 3, 3]),           # TC9 - Non-unique elements
    ([0, 0, -1, -1, 1], [-1, -1, 0, 0, 1]),       # TC10 - Zeros and negatives
]

def run_tests():
    for index, (original, expected) in enumerate(test_cases, start=1):
        print(f"\n---- TEST CASE {index} ----")
        print(f"Original: {original}, Expected: {expected}")
        
        pass_count = 0
        total_mutations = 10

        for mutation in range(1, total_mutations + 1):  # Run for each mutation
            mutated_output = mutate_merge_sort(original, mutation)
            if mutated_output == expected:
                pass_count += 1  # Count passing mutations
                print(f"Mutation {mutation} - Mutant Survives, with output {mutated_output}")
            else:
                print(f"Mutation {mutation} - Mutant Killed, with output {mutated_output}")

        # Calculate and print the mutation score
        mutation_score = (1 - (pass_count / total_mutations))* 100
        print(f"Mutation Score for TC{index}: {mutation_score:.2f}%\n")


if __name__ == "__main__":
    run_tests()
