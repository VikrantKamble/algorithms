"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.


"""


def find_peak_element(nums) -> int:
    """
    Since we need to find the peak element in O(log n) we
    have to do some kind of binary search, wherein in each
    step we are somehow able to eliminate half chunck of the
    search space. One important thing to notice is that the
    outside ends of the inputs are -inf, hence there has to be
    at least one peak element; unless and until the surface inside
    is constant i.e. all elements are the same. However, given the
    constraint that nums[i] != nums[i+1] for all i, this is eliminated.

    Extreme cases will be if the array is sorted in increasing order, in
    which case the last element will be the peak, vice versa, if the array
    is sorted in decreasing order, the first element will be the peak. We
    can utilize this condition for the binary search.
    """

    start, end = 0, len(nums) - 1

    # Base case is when start = end, i.e. a single element remains.
    while start < end:
        mid = (start + end) // 2

        # Only two cases less than and greater than
        # exists as no two elements are the same.
        if nums[mid] < nums[mid + 1]:
            # Think of sorted array
            start = mid + 1
        else:
            # Think of the reverse sorted array
            end = mid

    return start


if __name__ == "__main__":
    find_peak_element(nums=[3, 2, 5])
