"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 
"""


def can_jump_dp(nums) -> bool:
    last_index = len(nums) - 1

    # dp[i] represents if it is possible to reach the
    # last index from the index i.
    dp = [False] * len(nums)

    for k in range(len(nums) - 1, -1, -1):
        # easy case
        if k + nums[k] >= last_index:
            dp[k] = True
        elif nums[k] == 0:
            dp[k] = False
        else:
            can_jump_from_here = False

            # Check all possible jumps from this position.
            # If any of them reach the last index, break
            for j in range(nums[k], 0, -1):
                if dp[k + j]:
                    can_jump_from_here = True
                    break
            dp[k] = can_jump_from_here

    return dp[0]


def can_jump(nums) -> bool:
    """
    The difference compared to the previous solution, is that we constantly
    update the last index. We did not utlize the full information, that
    "when we jump, we ALWAYS jump to the RIGHT and not to the LEFT". Thus we
    OVERSOLVED the problem in the last solution. By oversolving I mean, that the
    last solution will also work for the case when the input has negative
    elements, i.e. we can jump both to right and to the left.
    """
    last_index = len(nums) - 1

    # If we are already at the end, we have reached the solution
    can_jump = True

    for k in range(len(nums) - 2, -1, -1):
        if k + nums[k] >= last_index:
            can_jump = True

            # We update the last index. We just need to
            # reach this new last index for the next iteration.
            last_index = k
        else:
            # last index will stay the same.
            can_jump = False

    return can_jump


if __name__ == "__main__":
    print(can_jump([3, 2, 1, 0, 4]))
