from typing import List


def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)

    for l in range(n // 2):
        for k in range(l, n - l - 1):
            (
                matrix[l][k],
                matrix[n - k - 1][l],
                matrix[n - l - 1][n - k - 1],
                matrix[k][n - l - 1],
            ) = (
                matrix[n - k - 1][l],
                matrix[n - l - 1][n - k - 1],
                matrix[k][n - l - 1],
                matrix[l][k],
            )

    print(matrix)


if __name__ == "__main__":
    # rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
