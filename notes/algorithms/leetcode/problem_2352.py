from typing import List


def equal_pairs(grid: List[List[int]]) -> int:
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            match = True
            for k in range(len(grid)):
                this_match = grid[i][k] == grid[k][j]
                match = match and this_match
                if not match:
                    break
            if match:
                count += 1

    return count


if __name__ == "__main__":
    res = equal_pairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])
    print(res)
