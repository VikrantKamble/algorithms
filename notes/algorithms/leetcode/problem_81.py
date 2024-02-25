from typing import List


def search_rotated(nums: List[int], target: int) -> bool:
    left = 0
    right = len(nums)

    while left <= right:

        print(left, right)

        mid = (left + right) // 2

        print(mid)

        if nums[mid] == target:
            return True

        if target < nums[mid]:
            if target <= nums[left]:
                if nums[left] >= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right = mid - 1
        else:
            if target >= nums[left]:
                if nums[left] >= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                left = mid + 1

    return False


if __name__ == "__main__":
    # res = search_rotated(nums=[2, 5, 6, 0, 0, 1, 2], target=3)

    # res = search_rotated(nums=[2, 5, 6, 10, 10, 11, 12, 0, 0, 1, 2], target=5)
    res = search_rotated(nums=[1, 0], target=0)

    print(res)
