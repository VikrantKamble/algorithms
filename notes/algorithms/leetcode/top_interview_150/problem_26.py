def remove_duplicates(nums):
    # base case:
    if len(nums) == 0:
        return 0

    curr_ele = nums[0]

    # This is the position we want to replace the next element
    last_pos = 1

    pos = 1

    while pos < len(nums):
        if nums[pos] != curr_ele:
            curr_ele = nums[pos]
            nums[last_pos] = curr_ele
            last_pos += 1
        pos += 1

    return last_pos


if __name__ == "__main__":
    print(remove_duplicates(nums=[1, 1, 2]))
