from typing import List


def find_min(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        # In a sorted array, mid is larger than the left
        # and smaller than the right. We check in which direction
        # the anomaly is present.
        mid = (left + right) // 2

        if nums[mid] < nums[left]:
            right = mid
        elif nums[mid] >= nums[right]:
            left = mid + 1
        else:
            break

    return nums[left]


if __name__ == "__main__":
    print(find_min(nums=[52, 1, 3, 4, 5, 12]))
