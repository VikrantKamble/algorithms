from typing import List


class Solution:

    def CanVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(index, visited) -> bool:
            # mark this index as visited
            visited.add(index)

            # Since this is a set, the only time it will be
            # equal in length to the number of rooms, is when
            # we have visisted all the rooms.
            if len(visited) == len(rooms):
                return True

            # recursively dfs on each of the possible rooms
            # from the room at index `index`
            for room_index in rooms[index]:
                if room_index not in visited:
                    if dfs(room_index, visited=visited):
                        return True

            return False

        return dfs(index=0, visited=set())


if __name__ == "__main__":
    solution = Solution()
    result = solution.CanVisitAllRooms(rooms=[[2, 3], [], [2], [1, 3]])
    print(result)
