def max_sub_array(nums):
    # This is a dynamic programming problem and
    # also called as Kadane's algorithm. We define dp[i]
    # as the maximum subarray ending on the index i. Now this
    # can be recursively defined as including the previous subarray
    # dp[i-1] or starting a new subarray with the solo element at
    # index i.
    dp = [0] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        if dp[i - 1] < 0:
            dp[i] = nums[i]
        else:
            dp[i] = dp[i - 1] + nums[i]

    return max(dp)


def max_sub_array_circular(nums) -> int:
    """
    In this case, we are going to track two things,
    the max subarray sum and the min subarray sum, ending
    at a given index i. The global maximum subarray sum will then
    be the max of the `max_subarray_sum` or `sum(nums) - min_subarray_sum`.
    """
    local_max, local_min = 0, float("inf")
    global_max, global_min = nums[0], nums[0]

    total = 0
    for ele in nums:
        # Keep track of the sum
        total += ele

        # Max subarray ending at a given index (Kadane's algorithm)
        local_max = max(ele, ele + local_max)
        if local_max > global_max:
            global_max = local_max

        # Min subarray ending at a given index.
        local_min = min(ele, ele + local_min)
        if local_min < global_min:
            global_min = local_min

    # Why do we need this extra check. This is only required
    # when all the elements of the input are negative. In that case,
    # global max is just going to be the least `negative` value, while
    # global min is going to be the entire array. If we simply did
    # max(global_max, total - global_min), we would end up returning 0,
    # which is incorrect.
    if global_max < 0:
        return global_max
    else:
        return max(global_max, total - global_min)


if __name__ == "__main__":
    # print(max_sub_array(nums=[5, 4, -1, 7, 8]))
    print(max_sub_array_circular(nums=[5, -3, 5]))
