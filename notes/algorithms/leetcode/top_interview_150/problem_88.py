"""
While merging two sorted arrays to create a new sorted array, we are
used to staring at the initial positions of both arrays, then checking 
the smallest element and updating the respective pointers. In this case
where we have to merge in-place, we need to start at the last positions
of both the arrays and find the largest element and then decrement the
respective pointer.
"""

from typing import List


def merge_new_list(nums1, nums2, m, n) -> None:
    i, j = 0, 0

    new_list = []
    while (i < m) and (j < n):
        if nums1[i] <= nums2[j]:
            new_list.append(nums1[i])
            i += 1
        else:
            new_list.append(nums2[j])
            j += 1

    if i == m:
        new_list.extend(nums2[j:])
    else:
        new_list.extend(nums1[i:])

    print(new_list)


def merge(nums1, nums2, m, n):
    # Traverse the arrays from the last positions and
    # choose the largest, and then start filling the
    # first array in place from the right.
    i, j = m - 1, n - 1

    k = m + n - 1

    while (i >= 0) and (j >= 0):
        # Element in the second array is the largest
        if nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            # Element in the first is the largest
            nums1[k] = nums1[i]
            i -= 1
        k -= 1

    if i < 0:
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
    elif j < 0:
        while i >= 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 13, 0, 0]
    nums2 = [2, 15]
    # merge_new_list(nums1=nums1, nums2=nums2, m=3, n=3)

    # merge([1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3)
    merge([0], [1], 0, 1)
