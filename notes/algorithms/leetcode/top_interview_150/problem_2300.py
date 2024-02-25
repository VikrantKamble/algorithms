def successfull_pairs(spells, potions, success):
    potions = sorted(potions)
    n = len(potions)

    def binary_search(nums, key) -> int:
        """Return index of equal or next higher value compared to key."""
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            # If there are repeated values, we want to
            # return the index of the first occurence.
            if nums[mid] >= key:
                end = mid
            else:
                start = mid + 1

        if nums[start] < key:
            return start + 1
        else:
            return start

    result = []
    for spell in spells:
        if success % spell == 0:
            req_potion = success // spell
        else:
            req_potion = success // spell + 1

        req_index = binary_search(potions, req_potion)
        result.append(n - req_index)

    return result


if __name__ == "__main__":
    res = successfull_pairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16)
    print(res)
