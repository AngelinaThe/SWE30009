# MERGE SORT ALGORITHM FROM https://github.com/B3ns44d/Python_Sorting_Algorithms/blob/master/Merge_Sort.py
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)

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

# Own written code to read and write data
if __name__ == "__main__":
    # Read input data from input_data.txt
    with open("SUT/input_data.txt", "r") as infile:
        input_lines = infile.readlines()

    sorted_results = []
    for line in input_lines:
        unsorted_list = list(map(int, line.strip().split(','))) 
        sorted_list = merge_sort(unsorted_list)
        sorted_results.append(sorted_list)

    for sorted_list in sorted_results:
        print("Sorted List:", ', '.join(map(str, sorted_list)))
