from typing import List


def unique_paths_with_obstacles(obstacle_grid: List[List[int]]) -> int:
    m, n = len(obstacle_grid), len(obstacle_grid[0])

    # Create an empty grid of max paths
    path_grid = []
    for _ in range(m):
        path_grid.append([0] * n)

    # base case
    if obstacle_grid[m - 1][n - 1] == 1:
        path_grid[m - 1][n - 1] = 0
    else:
        path_grid[m - 1][n - 1] = 1

    # edge case 1
    for k in range(m - 2, -1, -1):
        if obstacle_grid[k][n - 1] == 1:
            path_grid[k][n - 1] = 0
        else:
            path_grid[k][n - 1] = path_grid[k + 1][n - 1]

    # edge case 2
    for k in range(n - 2, -1, -1):
        if obstacle_grid[m - 1][k] == 1:
            path_grid[m - 1][k] = 0
        else:
            path_grid[m - 1][k] = path_grid[m - 1][k + 1]

    # Fill the rest of the grid cells
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            if obstacle_grid[j][i] == 1:
                path_grid[j][i] = 0
            else:
                path_grid[j][i] = path_grid[j][i + 1] + path_grid[j + 1][i]

    return path_grid[0][0]


if __name__ == "__main__":
    # res = unique_paths_with_obstacles([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    res = unique_paths_with_obstacles([[0, 0]])
    print(res)
