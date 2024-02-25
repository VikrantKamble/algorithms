from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    pos = 0

    merge_min, merge_max = new_interval[0], new_interval[1]

    merged = False
    merged_intervals = []
    while pos < len(intervals):

        this_interval = intervals[pos]

        # Case 1: non-overlapping (to the left)
        if merge_max < this_interval[0]:
            merged_intervals.append([merge_min, merge_max])
            merged_intervals.extend(intervals[pos:])

            merged = True

            break
        # Case 2: non-overlapping (to the right)
        if merge_min > this_interval[1]:
            # Add the current interval, but intervals to the right
            # might still overlap with the given interval.
            merged_intervals.append(this_interval)

        # Case 3: overlapping
        else:
            if (merge_min < this_interval[0]) and (merge_max <= this_interval[1]):
                merge_max = this_interval[1]
            elif (merge_min >= this_interval[0]) and (merge_max > this_interval[1]):
                merge_min = this_interval[0]
            elif (merge_min >= this_interval[0]) and (merge_max <= this_interval[1]):
                merge_min, merge_max = this_interval
            else:
                pass

        pos += 1

    if not merged:
        merged_intervals.append([merge_min, merge_max])
    return merged_intervals


if __name__ == "__main__":

    res = insert(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], new_interval=[4, 8]
    )
    res = insert([[3, 8], [9, 11]], new_interval=[3, 7])
    print(res)
