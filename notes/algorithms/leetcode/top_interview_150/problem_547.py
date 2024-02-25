from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        cities = set(range(len(isConnected)))
        number_of_provinces = 0

        def dfs(index, visited):
            # Mark this index as visited
            visited.add(index)

            # Visit every city directly connected with the
            # city at index `index`
            for city_index, is_connected in enumerate(isConnected[index]):
                if is_connected == 1:
                    if city_index not in visited:
                        dfs(city_index, visited)

        while len(cities) > 0:
            # Get all connected components (defined as a province)
            visited = set()
            dfs(cities.pop(), visited=visited)

            # update the count
            number_of_provinces += 1

            # Get cities that are reamining to be visited.
            cities = cities - visited

        return number_of_provinces


if __name__ == "__main__":
    solution = Solution()
    result = solution.findCircleNum(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(result)
