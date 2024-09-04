def split_and_sort(nums):

    # check input list length 
    if len(nums) > 30:
        print("Error: Input list should contain less number of integers.")
        return

    # filter numbers into two separate lists and remove duplicates
    pos_nums = sorted(list(set(num for num in nums if num > 0)))
    neg_nums = sorted(list(set(num for num in nums if num <= 0)))  # Include 0 as a negative number

    # print the lists
    print("Positive numbers:", pos_nums)
    print("Negative numbers:", neg_nums)

    return neg_nums, pos_nums
