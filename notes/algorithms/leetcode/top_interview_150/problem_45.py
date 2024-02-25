from typing import List


def jump_dp(nums: List[int]) -> int:
    last_index = len(nums) - 1

    # dp[i] represents the minimum number of jumps required to reach the
    # last index from the index i.
    dp = [0] * len(nums)

    # If we are at the last position, we don't need to jump
    dp[-1] = 0

    for k in range(len(nums) - 2, -1, -1):
        if k + nums[k] >= last_index:
            # We can reach the last position in one jump
            dp[k] = 1
        else:
            min_jumps_from_here = float("inf")

            # Check all possible jumps from this position.
            # If any of them reach the last index, break
            for j in range(nums[k], 0, -1):
                min_jumps_from_here = min(min_jumps_from_here, dp[k + j])
            dp[k] = 1 + min_jumps_from_here

    return dp[0]


def jump(nums: List[int]) -> int:
    num_steps = 0

    left, right = 0, 0
    while right < len(nums) - 1:
        # Here we compute the next range. We check
        # of all the positions in this range, what is the
        # fartest distance we can jump.
        longest = 0
        for i in range(left, right + 1):
            longest = max(longest, i + nums[i])
        left, right = right + 1, longest

        num_steps += 1

    return num_steps


if __name__ == "__main__":
    jump([1, 2, 1, 1, 4])
