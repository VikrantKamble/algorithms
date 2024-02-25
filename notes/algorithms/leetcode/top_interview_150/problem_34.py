from typing import List


def search_range(nums, target) -> List[int]:
    """
    Given an array of integers nums sorted in non-decreasing order,
    find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.
    """

    def get_range(left, right) -> List[int]:

        # Break case
        if left > right:
            return []

        # Base case, when we are down to a single element.
        if left == right:
            if (nums[left] == target) and (nums[right] == target):
                return [left, right]
            else:
                return []

        # Recursive case
        mid = (left + right) // 2

        if nums[mid] == target:
            # If mid equals targets, then we need to search both
            # sides as the target element can be present on both
            # sides of the mid since there are multiple of them.
            left_range = get_range(left=left, right=mid)
            right_range = get_range(left=mid + 1, right=right)

            if (len(left_range) == 0) and (len(right_range) > 0):
                this_range = right_range
            elif (len(left_range) > 0) and (len(right_range) == 0):
                this_range = left_range
            else:
                this_range = [left_range[0], right_range[1]]
        elif nums[mid] > target:
            this_range = get_range(left=left, right=mid - 1)
        else:
            this_range = get_range(left=mid + 1, right=right)

        return this_range

    res = get_range(left=0, right=len(nums) - 1)

    # If the target doesn't exists in the input list
    if len(res) == 0:
        return [-1, -1]
    return res


if __name__ == "__main__":
    print(search_range(nums=[], target=18))
