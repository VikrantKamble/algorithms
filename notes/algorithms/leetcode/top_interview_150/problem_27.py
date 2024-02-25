def remove_element(nums, val):
    # We start from the beginning and traverse the
    # array nums. At any point when the value equals the
    # target val, we swap it with the last position and
    # decrement the last position.

    # Base case
    if len(nums) == 0:
        return 0

    first, last = 0, len(nums) - 1
    while first < last:
        if nums[first] != val:
            first += 1
        else:
            if nums[last] == val:
                last -= 1
            else:
                nums[first], nums[last] = nums[last], nums[first]
                first += 1
                last -= 1

    # Edge case
    if nums[first] == val:
        return first
    else:
        return first + 1


if __name__ == "__main__":
    print(remove_element(nums=[2, 2, 2, 2, 2, 2, 2], val=2))
